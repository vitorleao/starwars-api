import httpx
import os

from functools import lru_cache
from dotenv import load_dotenv


class SWAPIClient:
    load_dotenv()
    BASE_URL = os.getenv("SWAPI_BASE_URL")

    @lru_cache(maxsize=32)
    def cached_fetch(self, endpoint: str):
        import asyncio

        return asyncio.run(self.fetch(endpoint))

    async def fetch(self, endpoint: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}{endpoint}")
            response.raise_for_status()
            data = response.json()
            return data.get("results", data)

    async def get_movies(self):
        return self.cached_fetch("films/")

    async def get_people(self):
        return self.cached_fetch("people/")

    async def get_planets(self):
        return self.cached_fetch("planets/")

    async def get_starships(self):
        return self.cached_fetch("starships/")
