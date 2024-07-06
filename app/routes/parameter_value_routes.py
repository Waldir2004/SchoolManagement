from fastapi import APIRouter, HTTPException
from controllers.parameter_value_controller import *
from models.parameter_value_model import ParameterValue

router = APIRouter()

nuevo_parametro = ParameterValueController()


@router.post("/create_parameter_value")
async def create_parameter_value(parameter_value: ParameterValue):
    rpta = nuevo_parametro.create_parameter_value(parameter_value)
    return rpta


@router.get("/get_parameter_value/{parameter_value_id}",response_model=ParameterValue)
async def get_parameter_value(parameter_value_id: int):
    rpta = nuevo_parametro.get_parameter_value(parameter_value_id)
    return rpta

@router.get("/get_parameters_values/")
async def get_parameters_values():
    rpta = nuevo_parametro.get_parameters_values()
    return rpta