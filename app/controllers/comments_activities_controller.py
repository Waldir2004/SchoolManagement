import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.comments_activities_model import comments_activities
from fastapi.encoders import jsonable_encoder

class Comments_activities_Controller:
        
    def create_comments_activities(self, comments_activities: comments_activities):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO comments_activities (activity_id, user_id, comment) VALUES (%s, %s, %s)", (comments_activities.activity_id, comments_activities.user_id, comments_activities.comment))
            conn.commit()
            conn.close()
            return {"resultado": "comments created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_comments_activities(self, comments_activities_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comments_activities WHERE id = %s", (comments_activities_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'activity_id':result[1],
                    'user_id':result[2],
                    'comment':result[3]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Comments not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_comments_activities(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comments_activities")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'activity_id':data[1],
                    'user_id':data[2],
                    'comment':data[3],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Comments not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_comments_activities(self, comments_activities_id:int, comments_activities:comments_activities):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE comments_activities SET activity_id = %s, user_id = %s, comment = %s WHERE id =%s", (comments_activities.activity_id, comments_activities.user_id, comments_activities.comment, comments_activities_id))
            conn.commit()
            conn.close()
            return {"resultado": "Comments edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_comments_activities(self, comments_activities_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM comments_activities WHERE id = %s", (comments_activities_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Comment eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()