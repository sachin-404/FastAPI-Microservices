[![Python application test and CI](https://github.com/sachin-404/FastAPI-Microservices/actions/workflows/devops.yml/badge.svg)](https://github.com/sachin-404/FastAPI-Microservices/actions/workflows/devops.yml)

# FastAPI Microservice


This project leverages FastAPI to create a microservice that interacts with Wikipedia. The microservice provides endpoints to interact with Wikipedia, allowing users to search for articles, retrieve summaries, extract noun phrases, and analyze parts of speech. It utilizes Docker for containerization, allowing for easy deployment and scalability. GitHub Actions are employed for continuous integration, running tests on each code push and automatically building and pushing Docker images to the Elastic Container Registry (ECR).

## GitHub Actions Workflow

GitHub Actions are set up to automate the testing and deployment process.

The workflow performs the following steps:

- **Checkout**: Checks out the repository's code.
- **Setup Python**: Sets up Python for the workflow.
- **Install Dependencies**: Installs project dependencies using pip.
- **Run Tests**: Runs tests using pytest.
- **Build Docker Image**: Builds the Docker image using the Dockerfile.
- **Push Docker Image**: Pushes the built Docker image to the Elastic Container Registry (ECR).

The workflow ensures that tests are run with each code push and that the - Docker image is automatically built and pushed to ECR, facilitating continuous integration and deployment.

## Endpoints

- **GET /**: Root endpoint, returns a welcome message.
- **GET /search/{name}**: Searches Wikipedia for articles related to the provided name.
- **GET /summary/{name}**: Retrieves a summary of the Wikipedia article with the provided name.
- **GET /phrase/{name}**: Extracts noun phrases from the Wikipedia article with the provided name.
- **GET /pos/{name}**: Analyzes the parts of speech in the Wikipedia article with the provided name.


