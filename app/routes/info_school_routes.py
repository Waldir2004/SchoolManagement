from fastapi import APIRouter, HTTPException
from controllers.info_school_controller import *
from models.info_school_model import SchoolInfo

router = APIRouter()

new = InfoSchoolController()


@router.post("/create_info_school")
async def create_info_school(school: SchoolInfo):
    rpta = new.create_info_school(school)
    return rpta


@router.get("/get_info_school/{info_school_id}",response_model=SchoolInfo)
async def get_info_school(info_school_id: int):
    rpta = new.get_info_school(info_school_id)
    return rpta

@router.get("/get_info_schools/")
async def get_info_schools():
    rpta = new.get_info_schools()
    return rpta

@router.put("/edit_info_school/{id}")
async def edit_info_school(id:int, school:SchoolInfo):
    rpta = new.edit_info_school(id,school)
    return rpta

@router.delete("/delete_info_school/{info_school_id}")
async def delete_info_schoolr(info_school_id: int):
    rpta = new.delete_info_school(info_school_id)
    return rpta