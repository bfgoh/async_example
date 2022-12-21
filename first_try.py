# How do we normally write a function
def f_normal():
    return "sync"


# This is a async function
async def f():
    return "async"


# print(type(f))
# print(type(f_normal))
# Both returns a function. Then what is the difference?


a = f()
print(a)
b = f_normal()
print(b)

a = f()
print(a)

# What if you want to access the value inside another function
# async def main():
#     value_wanted = await f()
#     print(value_wanted + "value in main")


# import asyncio

# # Create the event loop
# loop = asyncio.get_event_loop()  # Create a event loop
# # Get a couroutine from a sync function
# couroutine = f()
# print(loop.run_until_complete(couroutine))  # Runs
