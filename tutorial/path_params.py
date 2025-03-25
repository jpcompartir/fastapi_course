from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_current_user():
    return {"user_id": "current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/buildings/{building_id}")
async def get_building(building_id: int):
    building_dict = {
        1: "Eiffel Tower",
        2: "Empire State Building"
    }
    response = {
        "building_id": building_id,
        "building_name": building_dict[building_id]
    }
    
    return response