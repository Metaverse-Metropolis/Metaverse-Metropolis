# API Reference

This document provides the API reference for the Metaverse Metropolis AI Agent, describing the available endpoints, methods, and their usage.

## 1. Overview

The Metaverse Metropolis AI Agent exposes a RESTful API for interaction with the agent. The API allows you to send commands and receive responses in a structured format.

## 2. Authentication

All API requests must be authenticated using an API key. You can obtain your API key by registering on the platform.

### Example:

curl -X GET "https://api.metaverse-metropolis.com/agent-status" -H "Authorization: Bearer YOUR_API_KEY"

## 3. Endpoints

### GET /agent-status

Returns the current status of the AI Agent.

#### Response:

{
  "status": "active",
  "uptime": "12 hours",
  "last_action": "2025-01-31T10:00:00Z"
}

### POST /execute-action

Executes a specific action for the AI Agent.

#### Parameters:

- `action`: The action to be performed by the agent.
- `params`: A JSON object containing any parameters required for the action.

#### Example:

curl -X POST "https://api.metaverse-metropolis.com/execute-action" \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{"action": "start_task", "params": {"task_id": 12345}}'

### Response:

{
  "status": "success",
  "message": "Action executed successfully"
}

## 4. Error Codes

The API uses standard HTTP status codes to indicate success or failure.

- **200 OK**: Request was successful.
- **400 Bad Request**: Invalid input or parameters.
- **401 Unauthorized**: Missing or invalid API key.
- **500 Internal Server Error**: Something went wrong on the server side.
