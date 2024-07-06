import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.school_user_model import SchoolUser
from fastapi.encoders import jsonable_encoder

class SchoolUserController:
        
    def create_school_user(self, schoolUser: SchoolUser):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO schools_users (user_id, school_id) VALUES (%s, %s)", (schoolUser.user_id, schoolUser.school_id))
            conn.commit()
            conn.close()
            return {"resultado": "Creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_school_user(self, school_user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM schools_users WHERE id = %s", (school_user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'user_id':int(result[1]),
                    'school_id':int(result[2]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail=" not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_schools_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM schools_users")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'user_id':data[1],
                    'school_id':data[2],
                    'created_at':data[3],
                    'updated_at':data[4],
                    'deleted_at':data[5],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_school_user(self, school_user_id:int, schoolUser:SchoolUser):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE schools_users SET user_id= %s, school_id = %s WHERE id =%s", (schoolUser.user_id, schoolUser.school_id, school_user_id))
            conn.commit()
            conn.close()
            return {"resultado": "edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_school_user(self, school_user_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM schools_users WHERE id = %s", (school_user_id,))
            conn.commit()
            conn.close()
            return {"resultado": "eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
       
       