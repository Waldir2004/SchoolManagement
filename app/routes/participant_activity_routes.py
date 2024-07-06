from fastapi import APIRouter, HTTPException
from controllers.participant_activity_controller import *
from models.participant_activity_model import ParticipantActivity

router = APIRouter()

new = ParticipantActivityController()


@router.post("/create_participant_activity")
async def create_participant_activity(participant: ParticipantActivity):
    rpta = new.create_participant_activity(participant)
    return rpta


@router.get("/get_participant_activity/{id}",response_model=ParticipantActivity)
async def get_participant_activity(id: int):
    rpta = new.get_participant_activity(id)
    return rpta

@router.get("/get_participants_activities/")
async def get_participants_activities():
    rpta = new.get_participants_activities()
    return rpta

@router.put("/edit_participant_activity/{id}")
async def edit_participant_activity(id:int, participant:ParticipantActivity):
    rpta = new.edit_participant_activity(id,participant)
    return rpta

@router.delete("/delete_participant_activity/{id}")
async def delete_participant_activity(id: int):
    rpta = new.delete_participant_activity(id)
    return rpta