from flask import Flask, render_template, request
import sqlite3
import subprocess
import re

app = Flask(__name__)

DB_FILE = "employee_data.db"
TABLE_NAME = "employees"

def ask_llm(question):
    """Call Ollama LLM and extract SQL query."""
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", f"Convert this question into a SQL query for table {TABLE_NAME}: {question}"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        output = result.stdout.strip()
        match = re.search(r"```sql\s*(.*?)```", output, re.DOTALL | re.IGNORECASE)
        if match:
            sql_query = match.group(1).strip()
        else:
            lines = output.splitlines()
            sql_lines = [line for line in lines if re.match(r"^\s*(SELECT|UPDATE|DELETE|INSERT|WITH)\b", line, re.IGNORECASE)]
            sql_query = " ".join(sql_lines)
        return sql_query
    except Exception as e:
        return f"Error calling LLM: {e}"

def execute_sql(sql_query):
    """Execute SQL and return results as list of dicts."""
    conn = sqlite3.connect("employee_salary.db")
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        if cursor.description:
            columns = [desc[0] for desc in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            return result
        else:
            return [{"message": "Query executed successfully."}]
    except Exception as e:
        return [{"error": str(e)}]
    finally:
        conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    sql_query = ""
    results = []
    question = ""
    
    if request.method == "POST":
        question = request.form.get("question")
        action = request.form.get("action")
        
        if action == "Generate SQL":
            sql_query = ask_llm(question)
        elif action == "Execute SQL":
            sql_query = request.form.get("sql_query")
            results = execute_sql(sql_query)
    
    return render_template("index.html", question=question, sql_query=sql_query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
