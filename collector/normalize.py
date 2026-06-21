import json
from schema import FlowEvent

def safe_get(d, key, default=None):
    return d.get(key, default)

def normalize(flow):
    return FlowEvent(
        method=safe_get(flow, "method", "UNKNOWN"),
        url=safe_get(flow, "url", "UNKNOWN"),
        path=safe_get(flow, "path", None) or f"{safe_get(flow,'method','?')} {safe_get(flow,'url','?')}",
        status=safe_get(flow, "status"),
        size=int(safe_get(flow, "size", 0) or 0)
    ).__dict__

def run():
    try:
        with open("/data/flows.json") as f:
            raw = json.load(f)
    except:
        raw = []

    cleaned = [normalize(f) for f in raw]

    with open("/data/events.json", "w") as f:
        json.dump(cleaned, f, indent=2)

    print(f"[OK] normalized events: {len(cleaned)}")

if __name__ == "__main__":
    run()