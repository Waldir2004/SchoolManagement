import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.parameter_value_model import ParameterValue
from fastapi.encoders import jsonable_encoder

class ParameterValueController:
        
    def create_parameter_value(self, parameter_value: ParameterValue):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO parameters_values (parameter_id, name, description) VALUES (%s, %s, %s)", (parameter_value.parameter_id, parameter_value.name, parameter_value.description))
            conn.commit()
            conn.close()
            return {"resultado": "Parametro valor creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_parameter_value(self, parameter_value_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parameters_values WHERE id = %s", (parameter_value_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'parameter_id':int(result[1]),
                    'name':result[2],
                    'description':result[3],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Parameter not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_parameters_values(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parameters_values")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'parameter_id':data[1],
                    'name':data[2],
                    'description':data[3],
                    'created_at':data[4],
                    'updated_at':data[5],
                    'deleted_at':data[6],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Parameter not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    
       