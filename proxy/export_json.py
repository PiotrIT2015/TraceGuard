from mitmproxy import io
import json

flows = []

with open("/data/flows.mitm", "rb") as f:
    reader = io.FlowReader(f)

    for flow in reader.stream():
        flows.append({
            "method": flow.request.method,
            "url": flow.request.url,
            "status": flow.response.status_code if flow.response else None,
            "host": flow.request.host,
            "path": flow.request.path,
        })

with open("/data/flows.json", "w") as f:
    json.dump(flows, f, indent=2)