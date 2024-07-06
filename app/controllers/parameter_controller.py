import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.parameter_model import Parameter
from fastapi.encoders import jsonable_encoder

class ParameterController:
        
    def create_parameter(self, parameter: Parameter):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO parameters (reference, name, description) VALUES (%s, %s, %s)", (parameter.reference, parameter.name, parameter.description))
            conn.commit()
            conn.close()
            return {"resultado": "Parametro creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_parameter(self, parameter_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parameters WHERE id = %s", (parameter_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'reference':result[1],
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
       
    def get_parameters(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parameters")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'reference':data[1],
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
    
    def edit_parameter(self, parameter_id:int, parameter:Parameter):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE parameters SET reference= %s, name = %s, description = %s WHERE id =%s", (parameter.reference, parameter.name, parameter.description, parameter_id))
            conn.commit()
            conn.close()
            return {"resultado": "parameter edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_parameter(self, parameter_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM parameters WHERE id = %s", (parameter_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Parametro eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
       
       