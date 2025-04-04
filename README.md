# Clinical Diagnosis Extraction

This repository contains the codebase for the Clinical Diagnosis Extraction project.

## Development Setup

Follow these steps to set up the development environment:

1. **Install Dependencies**:
    Ensure you have Python and Poetry installed. Then, install the required dependencies:
    ```bash
    poetry install
    ```

## Building the Docker Image

To build and run the Docker image for this project:

1. **Build the Docker Image**:
    ```bash
    docker build -t clinical-diagnosis-extraction .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -p 8000:8000 clinical-diagnosis-extraction
    ```

3. **Access the Application**:
    Open your browser and navigate to `http://localhost:8000`.
