from fastapi import APIRouter, HTTPException
from controllers.reports_controller import *
from models.reports_model import reports
from models.user_model import User
from fastapi import APIRouter, Query
from typing import List

router = APIRouter()

nuevo_usuario = Reports_Controller()


@router.post("/create_reports")
async def create_reports(reports:reports):
    rpta = nuevo_usuario.create_reports(reports)
    return rpta

@router.get("/get_report/{id}")
async def get_report(id: int):
    rpta = nuevo_usuario.get_report(id)
    return rpta

@router.get("/get_reports")
async def get_reports():
    rpta = nuevo_usuario.get_reports()
    return rpta

@router.put("/edit_report/{id}")
async def edit_report(id:int, reports:reports):
    rpta = nuevo_usuario.edit_report(id,reports)
    return rpta

@router.delete("/delete_reports/{reports_id}")
async def delete_reports(reports_id: int):
    rpta = nuevo_usuario.delete_reports(reports_id)
    return rpta

@router.get("/search_users", response_model=List[User])
async def search_users(name: str = Query(..., min_length=1)):
    rpta = nuevo_usuario.search_users(name)
    return rpta