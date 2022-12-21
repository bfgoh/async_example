import requests
import pandas as pd
import time
import json

MAX_POKEMON = 151
POKEMON_ROOT = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_name_sync():
    pokemon_id = range(1, MAX_POKEMON + 1)
    results = []
    for id in pokemon_id:
        url_to_send = POKEMON_ROOT + str(id)
        print(f"Send Pokemon: {id}")
        res = requests.get(url_to_send)
        print(f"Receive Pokemon: {id}")
        # print(res.content.keys())
        record = json.loads(res.content)
        results.append(record["id"])
    df = pd.DataFrame(results)
    df.to_excel("pokemon_sync.xlsx", index=False)


if __name__ == "__main__":
    start_time = time.time()
    get_pokemon_name_sync()
    end_time = time.time()
    timetaken = end_time - start_time
    print(f"Time taken = {timetaken}")
