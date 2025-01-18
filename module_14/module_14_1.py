

import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(10/power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    print("Begin tournament")
    atask1 = asyncio.create_task(start_strongman('Pasha', 3))
    atask2 = asyncio.create_task(start_strongman('Denis', 4))
    atask3 = asyncio.create_task(start_strongman('Superman', 20))
    await atask1
    await atask2
    await atask3
    print("End tournament")

asyncio.run(start_tournament())