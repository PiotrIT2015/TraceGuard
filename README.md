# TraceGuard 

## Table of contents
* [General info](#general-info)
* [Running](#running)
* [Technologies](#technologies)

## General info
It is a lightweight, Docker-based mini SOC (Security Operations Center) for learning and experimenting with network traffic monitoring, MITM analysis, and basic threat detection.
It simulates a real-world security pipeline by collecting HTTP traffic, normalizing events, detecting anomalies, and visualizing security alerts in a simple dashboard.
The project is designed for educational purposes and helps demonstrate how security monitoring systems, proxies, and alert pipelines work together in modern observability and SOC environments.

| komponent     | adres                                          |
| ------------- | ---------------------------------------------- |
| API           | [http://localhost:5000](http://localhost:5000) |
| MITM proxy UI | [http://localhost:8081](http://localhost:8081) |
| Dashboard SOC | [http://localhost:8501](http://localhost:8501) |

## Running

curl.exe -X POST http://localhost:5000/login ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"piotr\",\"password\":\"1234\"}"
  
## Technologies
* Python 3.5
