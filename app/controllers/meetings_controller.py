import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.meetings_model import meetings
from fastapi.encoders import jsonable_encoder
from datetime import datetime

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
        
    def get_dicschools(self):
        try:    
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name FROM schools WHERE deleted_at IS NULL")
            schools = cursor.fetchall() 
    
            conn.close()
    
            return schools
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()

    def get_meetings(self, meetings_id: int):
        try:
            conn = get_db_connection()  # Asumiendo que esta función está definida en otro lugar
            cursor = conn.cursor()
            cursor.execute("""
            SELECT m.id, m.title, m.description, m.date, m.time, m.school_id, pv.name AS state 
            FROM meetings m 
            JOIN parameters_values pv ON m.state = pv.id 
            WHERE m.id = %s
            """, (meetings_id,))
            result = cursor.fetchone()
            if result:
                content = {
                'id': int(result[0]),
                'title': result[1],
                'description': result[2],
                'date': result[3],
                'time': result[4],
                'school_id': int(result[5]),
                'state': result[6]
            }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Meeting not found")
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Database error")
        finally:
            conn.close()

    def get_meetings(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            SELECT m.id, m.title, m.description, m.date, TIME_FORMAT(m.time, '%r') AS formatted_time, s.name AS school_name, pv.name AS state, m.created_at, 
            m.updated_at FROM meetings m JOIN schools s 
            ON m.school_id = s.id JOIN parameters_values pv ON m.state = pv.id WHERE m.deleted_at IS NULL;""")
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
            deleted_at = datetime.now()
            cursor.execute("UPDATE meetings SET deleted_at = %s WHERE id = %s", (deleted_at, meetings_id))
            conn.commit()
            return {"resultado": "Colegio eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()