from fastapi import APIRouter, HTTPException
from controllers.roles_controller import *
from models.roles_model import roles

router = APIRouter()

nuevo_usuario = Rol_Controller()


@router.post("/create_rol")
async def create_rol(roles:roles):
    rpta = nuevo_usuario.create_rol(roles)
    return rpta

@router.get("/get_rol/{id}")
async def get_Rol(id: int):
    rpta = nuevo_usuario.get_Rol(id)
    return rpta

@router.get("/get_rol")
async def get_rol():
    rpta = nuevo_usuario.get_rol()
    return rpta

@router.put("/edit_rol/{id}")
async def edit_rol(id:int, roles:roles):
    rpta = nuevo_usuario.edit_rol(id,roles)
    return rpta

@router.put("/delete_rol/{roles_id}")
async def delete_rol(roles_id: int):
    rpta = nuevo_usuario.delete_rol(roles_id)
    return rpta