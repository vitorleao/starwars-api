# Star Wars API (AWS & GCP Ready)

A RESTful API built with FastAPI that provides rich data about the Star Wars universe by consuming the public SWAPI. Designed for deployment on AWS Lambda/API Gateway and Google Cloud Platform (Cloud Functions/Run).

---

## Project Structure

```
starwars-api
├── app
│   ├── main.py               # Application entrypoint
│   ├── api
│   │   └── routes.py         # RESTful endpoints
│   ├── models
│   │   └── starwars.py       # Pydantic models
│   ├── services
│   │   └── swapi_client.py   # SWAPI integration logic
│   └── utils
│       └── helpers.py        # Utility functions
├── requirements.txt          # Dependencies
├── Dockerfile                # Docker build instructions
├── template.yaml             # AWS SAM template
├── .gcloudignore             # GCP ignore file
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
└── tests/                    # Unit and integration tests
```

---

## Prerequisites

- Python >= 3.9
- pip
- Docker (optional, for containerization)
- AWS CLI & AWS SAM CLI (for AWS deployment)
- Google Cloud SDK (for GCP deployment)

---

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd starwars-api
   ```

2. Install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## Running Locally

Start the API locally:
```
uvicorn app.main:app --reload
```
Access the API at: [http://127.0.0.1:8000/api/movies](http://127.0.0.1:8000/api/movies)

---

## Running with Docker

Build and run the Docker container:
```
docker build -t starwars-api .
docker run -p 8000:8000 starwars-api
```

---

## Example Requests

- Get all movies:
  ```
  GET /api/movies
  ```
- Get all characters:
  ```
  GET /api/characters
  ```
- Filter movies by year and title:
  ```
  GET /api/filter/movies?year=1977&title=hope
  ```
- Sort characters alphabetically:
  ```
  GET /api/sort/characters?sort_by=name
  ```

---

## API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Rate Limiting

The API enforces rate limiting (default: 10 requests per minute per IP). If you exceed the limit, you will receive a 429 error.

---

## Code Formatting

This project uses [Black](https://black.readthedocs.io/) for code formatting.  
To format all Python files, run:

```
black .
```

---

## Testing

Run unit and integration tests:
```
pip install pytest pytest-asyncio pytest-mock
pytest --cov=app
```

---

## Deploying to AWS Lambda & API Gateway

1. Build and deploy using AWS SAM:
   ```
   sam build
   sam deploy --guided
   ```
2. The API will be available via API Gateway.

---

## Deploying to Google Cloud Platform

1. Build the Docker image:
   ```
   docker build -t starwars-api .
   ```
2. Deploy to Cloud Run:
   ```
   gcloud builds submit --tag gcr.io/<PROJECT_ID>/starwars-api
   gcloud run deploy starwars-api --image gcr.io/<PROJECT_ID>/starwars-api --platform managed
   ```
3. Configure API Gateway as per GCP documentation.

---

## Architecture Diagram

```mermaid
graph TD
    GW[API Gateway] --> FN[Lambda/Cloud Function (FastAPI)]
    FN --> SWAPI[swapi.dev]
```

---

## Author

[Vitor Leão](https://vitorleao.github.io/)
