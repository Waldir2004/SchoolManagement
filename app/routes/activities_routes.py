from fastapi import APIRouter, HTTPException
from controllers.activities_controller import *
from models.activities_model import activities

router = APIRouter()

nuevo_usuario = Activities_Controller()


@router.post("/create_activities")
async def create_activities(activities:activities):
    rpta = nuevo_usuario.create_activities(activities)
    return rpta

@router.get("/get_activity/{id}")
async def get_activity(id: int):
    rpta = nuevo_usuario.get_activity(id)
    return rpta

@router.get("/get_activities")
async def get_activities():
    rpta = nuevo_usuario.get_activities()
    return rpta

@router.put("/edit_activities/{id}")
async def edit_activities(id:int, activities:activities):
    rpta = nuevo_usuario.edit_activities(id,activities)
    return rpta

@router.delete("/delete_activities/{activities_id}")
async def delete_activities(activities_id: int):
    rpta = nuevo_usuario.delete_activities(activities_id)
    return rpta