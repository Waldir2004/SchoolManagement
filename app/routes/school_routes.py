from fastapi import APIRouter, HTTPException
from controllers.schools_controller import *
from models.schools_model import schools

router = APIRouter()

nuevo_usuario = Schools_Controller()


@router.post("/create_Schools")
async def create_Schools(Schools:schools):
    rpta = nuevo_usuario.create_Schools(Schools)
    return rpta

@router.get("/get_schools/{id}")
async def get_schools(id: int):
    rpta = nuevo_usuario.get_schools(id)
    return rpta

@router.get("/get_schools")
async def get_schools():
    rpta = nuevo_usuario.get_schools()
    return rpta

@router.put("/edit_school/{id}")
async def edit_school(id:int, schools:schools):
    rpta = nuevo_usuario.edit_school(id,schools)
    return rpta

@router.delete("/delete_school/{schools_id}")
async def delete_school(schools_id: int):
    rpta = nuevo_usuario.delete_school(schools_id)
    return rpta

@router.get("/get_parameter_values/{parameter_id}")
def get_parameter_values(parameter_id: int):
    return nuevo_usuario.get_parameter_values(parameter_id)