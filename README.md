<img src="https://github.com/user-attachments/assets/efeb3449-1a43-4764-857a-2699c81e7f40" width="500" height="200"/>

# E-commerce Recommendation System

This project aims to build a real-time e-commerce recommendation system using Apache Flink. The data stream is handled by Apache Kafka, and the project is containerized using Docker for easy deployment.

## Project Overview

This project focuses on building a recommendation system that provides product recommendations to users based on their interests in an e-commerce platform. The system processes real-time data using **Apache Flink** and streams data through **Apache Kafka**. Docker is used to containerize the services, allowing for easy deployment and scalability.

### Technologies Used
- **Apache Flink**: Used for processing real-time data streams.
- **Apache Kafka**: Used for real-time data transmission between services.
- **Docker**: Containerizes the Kafka, Flink, and other services for easier management.
- **Python**: Used to integrate Apache Flink with Kafka and process the data streams.

### Requirements

- Docker (to manage the containerized Flink and Kafka services)
- Python 3.x
- Kafka and Flink Docker images
- Apache Flink and Kafka Python SDKs
1. **Install Docker:**
   - Download and install Docker from the [official Docker website](https://www.docker.com/get-started).

2. **Start Flink and Kafka Docker Containers:**
   -To start the Flink and Kafka services using Docker Compose, run the following command in your terminal:
3. **Create Docker Kafka  :**
   -To build docker make sure you have connected docker and use this:
   ```docker-compose up -d```
   - one of the important note:if you see some error with server.properties file you will may modifie this file.(i cannot share this file because of the api passwords but i can help you on my mail)

### Project structure
 ```
    flink-e-commerce-project/
│
├── docker-compose.yml         # Docker Compose file to set up Kafka and Flink
├── consumer.py          # Flink consumer for processing the data stream
├── producer.py          # Kafka producer for sending data to Kafka
└── README.md
 ```

### Communication
- nursenabaykir@gmail.com

