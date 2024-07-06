import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.activities_model import activities
from fastapi.encoders import jsonable_encoder

class Activities_Controller:
        
    def create_activities(self, activities: activities):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO activities (title, description, start_date, end_date, school_id, state_id) VALUES (%s, %s, %s, %s, %s, %s)", (activities.title, activities.description, activities.start_date, activities.end_date, activities.school_id, activities.state_id ))
            conn.commit()
            conn.close()
            return {"resultado": "Activities created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_activity(self, activities_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM activities WHERE id = %s", (activities_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'title':result[1],
                    'description':result[2],
                    'start_date':result[3],
                    'end_date':result[4],
                    'school_id':result[5],
                    'state_id':result[6]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Activities not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            

    def get_activities(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM activities")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'title':data[1],
                    'description':data[2],
                    'start_date':data[3],
                    'end_date':data[4],
                    'school_id':data[5],
                    'state_id':data[6],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Activities not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_activities(self, activities_id:int, activities:activities):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE activities SET title = %s, description = %s, start_date = %s, end_date = %s, school_id = %s, state_id = %s WHERE id =%s", (activities.title, activities.description, activities.start_date, activities.end_date, activities.school_id, activities.state_id, activities_id))
            conn.commit()
            conn.close()
            return {"resultado": "Activities edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_activities(self, activities_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM activities WHERE id = %s", (activities_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Activities eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()