import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.roles_model import roles
from fastapi.encoders import jsonable_encoder

class Rol_Controller:
        
    def create_rol(self, roles: roles):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO roles (name, state) VALUES (%s, %s)", (roles.name, roles.state))
            conn.commit()
            conn.close()
            return {"resultado": "Rol created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_Rol(self, Rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (Rol_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'name':result[1],
                    'state':result[2]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_rol(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'name':data[1],
                    'state':data[2]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_rol(self, roles_id:int, roles:roles):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE roles SET name = %s, state = %s WHERE id =%s", (roles.name, roles.state, roles_id))
            conn.commit()
            conn.close()
            return {"resultado": "Rol edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_rol(self, roles_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM roles WHERE id = %s", (roles_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Rol eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()