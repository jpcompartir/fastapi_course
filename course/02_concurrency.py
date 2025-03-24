import fastapi

async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers

burgers = await get_burgers(2)


@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers