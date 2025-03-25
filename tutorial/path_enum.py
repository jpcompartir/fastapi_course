from fastapi import FastAPI
from enum import Enum
from typing import Dict, Any

app = FastAPI()

class BuildingName(str, Enum):
    empire = "Empire State Building"
    eiffel = "Eiffel Tower"
    liberty = "Statue of Liberty"

building_info_dict: Dict[BuildingName, Dict[str, Any]] = {
    BuildingName.empire: {"location": "New York, USA", "height": "381m"},
    BuildingName.eiffel: {"location": "Paris, France", "height": "330m"},
    BuildingName.liberty: {"location": "New York, USA", "height": "93m"}
}

@app.get("/buildings/{building_name}")
async def get_building(building_name: BuildingName):
    if building_name in building_info_dict:
        return {"name": building_name,
                **building_info_dict[building_name]}
    
    
# @app.get("/buildings/{building_name}")
# async def get_building(building_name: BuildingName):
#     if building_name is BuildingName.eiffel:
#         return {"building_name": building_name, "location": "Paris, the city of love."}
    
#     if building_name.value == "Empire State Building":
#         return {"building_name": building_name, "location": "New York, the city that never sleeps."}
    
#     return {"building_name": building_name, "location": "New York, the city that never sleeps"}


