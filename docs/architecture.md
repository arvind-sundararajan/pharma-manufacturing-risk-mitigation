# Architecture Overview
The Pharmaceutical Manufacturing Risk Mitigation Engine is designed as a microservices-based architecture, with the following components:

* **Risk Assessment Service**: responsible for evaluating the risk of a given manufacturing process
* **Data Ingestion Service**: responsible for collecting and processing data from various sources
* **Data Storage**: a relational database management system for storing and retrieving data
* **API Gateway**: handles incoming requests and routes them to the appropriate service

## Risk Assessment Service
The Risk Assessment Service is built using a machine learning model, trained on historical data to predict the likelihood of a given process resulting in a defective product.

## Data Ingestion Service
The Data Ingestion Service is responsible for collecting data from various sources, including sensors, machines, and manual input.

## Data Storage
The Data Storage component is a PostgreSQL database, used to store and retrieve data for the Risk Assessment Service and Data Ingestion Service.

## API Gateway
The API Gateway is built using Flask, and handles incoming requests from clients, routing them to the appropriate service.