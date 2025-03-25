from fastapi import FastAPI

app = FastAPI()

@app.get("/buildings")
async def return_empire_state():
    return {"building_name": "Empire State Building"}


@app.get("/buildings")
async def return_eiffel_tower():
    return {"building_name": "Eiffel Tower"}