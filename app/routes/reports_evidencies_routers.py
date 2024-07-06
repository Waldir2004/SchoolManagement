from fastapi import APIRouter, HTTPException
from controllers.reports_evidencies_controller import *
from models.reports_evidencies_model import reports_evidencies

router = APIRouter()

nuevo_usuario = Reports_evidencies_Controller()


@router.post("/create_report_evidencies")
async def create_reports_evidencies(reports_evidencies:reports_evidencies):
    rpta = nuevo_usuario.create_reports_evidencies(reports_evidencies)
    return rpta

@router.get("/get_report_evidencies/{id}")
async def get_repor_evidencies(id: int):
    rpta = nuevo_usuario.get_report_evidencies(id)
    return rpta

@router.get("/get_reports_evidencies")
async def get_reports_evidencies():
    rpta = nuevo_usuario.get_reports_evidencies()
    return rpta

@router.put("/edit_report_evidencies/{id}")
async def edit_report(id:int, reports_evidencies:reports_evidencies):
    rpta = nuevo_usuario.edit_report_evidencies(id,reports_evidencies)
    return rpta

@router.delete("/delete_reports_evidencies/{reports_evidencies_id}")
async def delete_reports_evidencies(reports_evidencies_id: int):
    rpta = nuevo_usuario.delete_reports_evidencies(reports_evidencies_id)
    return rpta