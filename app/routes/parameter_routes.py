from fastapi import APIRouter, HTTPException
from controllers.parameter_controller import *
from models.parameter_model import Parameter

router = APIRouter()

nuevo_parametro = ParameterController()


@router.post("/create_parameter")
async def create_parameter(parameter: Parameter):
    rpta = nuevo_parametro.create_parameter(Parameter)
    return rpta


@router.get("/get_parameter/{parameter_id}",response_model=Parameter)
async def get_parameter(parameter_id: int):
    rpta = nuevo_parametro.get_parameter(parameter_id)
    return rpta

@router.get("/get_parameters/")
async def get_parameters():
    rpta = nuevo_parametro.get_parameters()
    return rpta

@router.put("/edit_parameter/{id}")
async def edit_parameter(id:int, parameter:Parameter):
    rpta = nuevo_parametro.edit_parameter(id,parameter)
    return rpta

@router.delete("/delete_parameter/{parameter_id}")
async def delete_parameter(parameter_id: int):
    rpta = nuevo_parametro.delete_parameter(parameter_id)
    return rpta