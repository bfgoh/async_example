import pandas as pd
import asyncio
import aiohttp
import time

MAX_POKEMON = 500
POKEMON_ROOT = "https://pokeapi.co/api/v2/pokemon/"


async def get_data(session, id, url):
    print(f"Send Pokemon {id}")
    async with session.get(url) as resp:
        response_json = await resp.json()
        print(f"Receive Pokemon {id}")
        response_json = response_json["id"]
        return response_json


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for id in range(1, MAX_POKEMON + 1):
            url_to_send = POKEMON_ROOT + str(id)
            task = get_data(session, id, url_to_send)
            tasks.append(task)
        result = await asyncio.gather(*tasks)
    result_df = pd.DataFrame(result)
    result_df.to_excel("pokemon_async.xlsx", index=False)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    timetaken = end_time - start_time
    print(f"Time taken = {timetaken}")
