# Usage Guide
## Prerequisites
* Docker installed on the system
* A PostgreSQL database instance

## Running the Application
1. Clone the repository: `git clone https://github.com/your-username/pharma-manufacturing-risk-mitigation.git`
2. Change into the repository directory: `cd pharma-manufacturing-risk-mitigation`
3. Build the Docker image: `docker build -t pharma-risk-mitigation .`
4. Run the Docker container: `docker run -p 5000:5000 pharma-risk-mitigation`

## API Endpoints
The API Gateway exposes the following endpoints:

* **POST /assess-risk**: evaluates the risk of a given manufacturing process
* **POST /ingest-data**: collects and processes data from various sources

## Example Usage
```bash
# Assess risk of a manufacturing process
curl -X POST -H "Content-Type: application/json" -d '{"process_id": 123, "parameters": {"temperature": 25, "pressure": 100}}' http://localhost:5000/assess-risk

# Ingest data from a sensor
curl -X POST -H "Content-Type: application/json" -d '{"sensor_id": 456, "reading": 50}' http://localhost:5000/ingest-data
```