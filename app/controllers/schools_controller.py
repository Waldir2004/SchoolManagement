import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.schools_model import schools
from fastapi.encoders import jsonable_encoder

class Schools_Controller:
        
    def create_Schools(self, school: schools):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO schools (name, state) VALUES (%s, %s)", (school.name, school.state))
            conn.commit()
            conn.close()
            return {"resultado": "school created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_schools(self, schools_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM schools WHERE id = %s", (schools_id,))
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
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_schools(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM schools")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'name':data[1],
                    'state':data[2],
                    'created_at':data[3]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="School not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_school(self, school_id:int, school:schools):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE schools SET name = %s, state = %s WHERE id =%s", (school.name, school.state, school_id))
            conn.commit()
            conn.close()
            return {"resultado": "school edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_school(self, school_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM schools WHERE id = %s", (school_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Colegio eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
       
