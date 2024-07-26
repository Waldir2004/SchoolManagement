from fastapi import APIRouter, HTTPException
from controllers.meetings_controller import *
from models.meetings_model import meetings

router = APIRouter()

nuevo_usuario = meetings_Controller()


@router.post("/create_meetings")
async def create_meetings(meetings:meetings):
    rpta = nuevo_usuario.create_meetings(meetings)
    return rpta

@router.get("/get_meetings/{id}")
async def get_meetings(id: int):
    rpta = nuevo_usuario.get_meetings(id)
    return rpta

@router.get("/get_dicschools")
async def get_dicschools():
    rpta = nuevo_usuario.get_dicschools()
    return rpta


@router.get("/get_meetings")
async def get_meetings():
    rpta = nuevo_usuario.get_meetings()
    return rpta

@router.put("/edit_meetings/{id}")
async def edit_meetings(id:int, meetings:meetings):
    rpta = nuevo_usuario.edit_meetings(id,meetings)
    return rpta

@router.delete("/delete_meetings/{meetings_id}")
async def delete_meetings(meetings_id: int):
    rpta = nuevo_usuario.delete_meetings(meetings_id)
    return rpta