# Natural-language-to-SQL
AI-powered system to generate and execute SQL queries on employee data. Converts natural language questions into SQL using an LLM and returns query results from a SQLite database.
An AI-powered system that converts natural language questions into SQL queries for employee data stored in SQLite. Users can generate SQL using an LLM and execute it directly from a Flask web interface.

## Features
- Convert plain English questions into SQL queries
- Execute SQL queries on SQLite database
- View results in a web interface
- Supports employee salary, department, position, and other attributes
- Integration with Ollama LLM for query generation

## Requirements
- Python 3.8+
- Flask
- SQLite3 (built-in)
- Pandas
- Ollama LLM (mistral model)

Install dependencies:

```bash
pip install Flask pandas
