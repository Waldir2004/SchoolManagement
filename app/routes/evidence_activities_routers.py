from fastapi import APIRouter, HTTPException
from controllers.evidence_activities_controller import *
from models.evidence_activities_model import evidence_activities

router = APIRouter()

nuevo_usuario = Evidence_activities_Controller()


@router.post("/create_evidence_activities")
async def create_evidence_activities(evidence_activities:evidence_activities):
    rpta = nuevo_usuario.create_evidence_activities(evidence_activities)
    return rpta

@router.get("/get_evidence_activities/{id}")
async def get_evidence_activities(id: int):
    rpta = nuevo_usuario.get_evidence_activities(id)
    return rpta

@router.get("/get_evidence_activities")
async def get_evidence_activities():
    rpta = nuevo_usuario.get_evidence_activities()
    return rpta

@router.put("/edit_evidence_activities/{id}")
async def edit_comments_activities(id:int, evidence_activities:evidence_activities):
    rpta = nuevo_usuario.edit_comments_evidence_activities(id,evidence_activities)
    return rpta

@router.delete("/delete_evidence_activities/{evidence_activities_id}")
async def delete_evidence_activities(evidence_activities_id: int):
    rpta = nuevo_usuario.delete_evidence_activities(evidence_activities_id)
    return rpta