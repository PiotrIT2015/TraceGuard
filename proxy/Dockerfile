FROM python:3.11-slim

RUN pip install mitmproxy

COPY export_json.py /export_json.py

EXPOSE 8080 8081

CMD sh -c "mitmweb --web-host 0.0.0.0 --listen-port 8080 -w /data/flows.mitm & sleep 5 && python /export_json.py"