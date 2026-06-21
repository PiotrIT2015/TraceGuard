from mitmproxy import io
import json

flows = []

with open("/data/flows.mitm", "rb") as f:
    reader = io.FlowReader(f)

    for flow in reader.stream():
        flows.append({
            "method": flow.request.method,
            "url": flow.request.url,
            "path": flow.request.path,
            "host": flow.request.host,
            "status": flow.response.status_code if flow.response else None,
            "size": len(flow.request.content or b""),
        })

with open("/data/flows.json", "w") as f:
    json.dump(flows, f, indent=2)