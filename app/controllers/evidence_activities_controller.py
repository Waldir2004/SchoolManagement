import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.evidence_activities_model import evidence_activities
from fastapi.encoders import jsonable_encoder

class Evidence_activities_Controller:
        
    def create_evidence_activities(self, evidence_activities: evidence_activities):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO evidence_activities (activity_id, type_id, uploaded_by) VALUES (%s, %s, %s)", (evidence_activities.activity_id, evidence_activities.type_id, evidence_activities.uploaded_by))
            conn.commit()
            conn.close()
            return {"resultado": "Evidence created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_evidence_activities(self, evidence_activities_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM evidence_activities WHERE id = %s", (evidence_activities_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'activity_id':result[1],
                    'type_id':result[2],
                    'uploaded_by':result[4]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Evidence not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_evidence_activities(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM evidence_activities")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'activity_id':data[1],
                    'type_id':data[2],
                    'uploaded_by':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Evidence not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_comments_evidence_activities(self, evidence_activities_id:int, evidence_activities:evidence_activities):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE evidence_activities SET activity_id = %s, type_id = %s, uploaded_by = %s WHERE id =%s", (evidence_activities.activity_id, evidence_activities.type_id, evidence_activities.uploaded_by, evidence_activities_id))
            conn.commit()
            conn.close()
            return {"resultado": "Evidence edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_evidence_activities(self, evidence_activities_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM evidence_activities WHERE id = %s", (evidence_activities_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Evidence eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()