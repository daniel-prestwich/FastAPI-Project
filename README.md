# Prompt API

A FastAPI application demonstrating MCP tool use cases.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/status` | Returns API status |
| POST | `/echo` | Echoes a message back |
| GET | `/prompts/templates` | Returns vetted system prompt templates by agent role |

The `/prompts/templates` endpoint is the core MCP use case — it gives Copilot access to curated, domain-specific prompt templates it wouldn't otherwise have.

## Running locally

```bash
uvicorn main:app --reload
```

API docs available at `http://localhost:8000/docs`

## Deployment

Hosted on Azure App Service and exposed via Azure API Management as an MCP server.

```bash
az webapp up --name API-to-MCP --resource-group rg-sample-api --runtime "PYTHON:3.11" --location swedencentral
```
