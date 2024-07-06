import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.participant_meeting_model import ParticipantMeeting
from fastapi.encoders import jsonable_encoder

class ParticipantMeetingController:
        
    def create_participant_meeting(self, participant: ParticipantMeeting):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO participants_meetings (meeting_id, type_id, user_id, state) VALUES (%s, %s, %s, %s)", (participant.meeting_id, participant.type_id, participant.user_id, participant.state))
            conn.commit()
            conn.close()
            return {"resultado": "creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_participant_meeting(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM participants_meetings WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'meeting_id':int(result[1]),
                    'type_id':int(result[2]),
                    'user_id':int(result[3]),
                    'state':int(result[4]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_participants_meetings(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM participants_meetings")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'meeting_id':data[1],
                    'type_id':data[2],
                    'user_id':data[3],
                    'state':data[4],
                    'created_at':data[5],
                    'updated_at':data[6],
                    'deleted_at':data[7],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail=" not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_participant_meeting(self, id:int, participant:ParticipantMeeting):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE participants_meetings SET meeting_id= %s, type_id= %s, user_id = %s, state = %s WHERE id =%s", (participant.meeting_id, participant.type_id, participant.user_id, participant.state, id))
            conn.commit()
            conn.close()
            return {"resultado": "edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_participant_meeting(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM participants_meetings WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
       
       