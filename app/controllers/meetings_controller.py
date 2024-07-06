import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.meetings_model import meetings
from fastapi.encoders import jsonable_encoder

class meetings_Controller:
        
    def create_meetings(self, meetings: meetings):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO meetings (title, description, date, time, school_id, state) VALUES (%s, %s, %s, %s, %s, %s)", (meetings.title, meetings.description, meetings.date, meetings.time, meetings.school_id, meetings.state))
            conn.commit()
            conn.close()
            return {"resultado": "Meetings created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_meetings(self, meetings_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM meetings WHERE id = %s", (meetings_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'title':result[1],
                    'description':result[2],
                    'date':result[3],
                    'time':result[4],
                    'school_id':result[5],
                    'state':result[6]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Meetings not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_meetings(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM meetings")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':int(data[0]),
                    'title':data[1],
                    'description':data[2],
                    'date':data[3],
                    'time':data[4],
                    'school_id':data[5],
                    'state':data[6]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Meetings not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_meetings(self, meetings_id:int, meetings:meetings):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE meetings SET title = %s, description = %s, date = %s, time = %s, school_id = %s, state = %s WHERE id =%s", (meetings.title, meetings.description, meetings.date, meetings.time, meetings.school_id, meetings.state, meetings_id))
            conn.commit()
            conn.close()
            return {"resultado": "Meetings edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_meetings(self, meetings_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM meetings WHERE id = %s", (meetings_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Meetings eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()