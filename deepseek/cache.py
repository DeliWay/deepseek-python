from typing import Dict, Optional
import time

class SimpleCache:
    def __init__(self, ttl: int = 3600):
        self.cache: Dict[str, dict] = {}
        self.ttl = ttl  # Время жизни кеша в секундах

    def get(self, key: str) -> Optional[dict]:
        if key in self.cache:
            cached_time, response = self.cache[key]
            if time.time() - cached_time < self.ttl:
                return response
            del self.cache[key]
        return None

    def set(self, key: str, value: dict):
        self.cache[key] = (time.time(), value)