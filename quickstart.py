import asyncio, time

# Now we have our first async function written. Lets look at
async def example_similar_to_sync_function():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


async def run_with_id(id):
    print(f"Hello! {id}")
    print(f"{id} waiting start")
    await asyncio.sleep(1.0)
    print(f"{id} waiting end")
    print(f"Bye! {id}")


async def main():
    tasks = []
    for i in range(1, 5):
        task = asyncio.create_task(run_with_id(i))
        tasks.append(task)
    all_tasks = await asyncio.gather(*tasks)


# asyncio.run(main())
asyncio.run(example_similar_to_sync_function())
