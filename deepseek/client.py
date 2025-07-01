import requests
import aiohttp
from typing import Optional
from .cache import SimpleCache


class DeepSeek:
    def __init__(self, api_key: str = None, base_url: str = "https://api.deepseek.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache = SimpleCache()

    def generate(self, prompt: str, model: str = "deepseek-chat", use_cache: bool = True) -> str:
        """Синхронный запрос к API."""
        cache_key = f"{model}:{prompt}"
        if use_cache and (cached_response := self.cache.get(cache_key)):
            return cached_response["choices"][0]["message"]["content"]

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=data,
        )
        response.raise_for_status()
        result = response.json()

        if use_cache:
            self.cache.set(cache_key, result)
        return result["choices"][0]["message"]["content"]

    async def generate_async(self, prompt: str, model: str = "deepseek-chat") -> str:
        """Асинхронный запрос к API."""
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            data = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
            }
            async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
            ) as response:
                response.raise_for_status()
                result = await response.json()
                return result["choices"][0]["message"]["content"]