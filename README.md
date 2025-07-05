# AI-Driven PDF Generation Service

This project is a fully functional MVP for an AI-driven PDF generation service using FastAPI and DocuForge.

## Features

-   **FastAPI Endpoint**: Exposes a GET endpoint `/render` that accepts a prompt and an optional title.
-   **Streaming PDF Response**: Returns a PDF file rendered as a streaming HTTP response.
-   **Agent-Based Architecture**: Uses an `AgentController` to manage the PDF generation process.
-   **Structured Logging**: Implements robust logging with `loguru` to track requests and errors.
-   **Containerized**: Includes a `Dockerfile` and `docker-compose.yml` for easy deployment.
-   **Unit Tested**: Comes with a suite of unit tests for the core application logic.

## Getting Started

### Prerequisites

-   Python 3.11
-   Docker and Docker Compose
-   A local installation of the `docuforge` library.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Unit Tests

To ensure that the application is working correctly, you can run the unit tests using `pytest`:

```bash
pytest
```

### Running the Application

You can run the application in one of two ways:

**1. Directly with Uvicorn (for local development):**

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

**2. With Docker Compose:**

If you have a local copy of the `docuforge` repository in the parent directory of this project, you can run the application using Docker Compose:

```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`.

## Usage

Once the application is running, you can generate a PDF by sending a GET request to the `/render` endpoint.

### Example with `curl`

```bash
curl -X GET "http://127.0.0.1:8000/render?prompt=This%20is%20a%20test%20of%20the%20PDF%20generation%20service.&title=TestDocument" -o output.pdf
```

This command will generate a PDF named `TestDocument.pdf` with the content "This is a test of the PDF generation service." and save it as `output.pdf`.

### Example in Browser

You can also generate a PDF by visiting the following URL in your browser:

```
http://127.0.0.1:8000/render?prompt=This%20is%20a%20test%20of%20the%20PDF%20generation%20service.&title=TestDocument
```

This will download a PDF file named `TestDocument.pdf`.
