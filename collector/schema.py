from dataclasses import dataclass
from typing import Optional

@dataclass
class FlowEvent:
    method: str = "UNKNOWN"
    url: str = "UNKNOWN"
    path: str = "UNKNOWN"
    status: Optional[int] = None
    size: int = 0