import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder

class UserController:
    def create_user(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (role_id, name, last_name, email, phone, document_type_id, document_number, password, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (user.role_id, user.name, user.last_name, user.email, user.phone, user.document_type_id, user.document_number, user.password, user.state))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'role_id':int(result[1]),
                    'name':result[2],
                    'last_name':result[3],
                    'email':result[4],
                    'phone':result[5],
                    'document_type_id':int(result[6]),
                    'document_number':result[7],
                    'password':result[8],
                    'state':int(result[9]),
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
       
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'role_id':data[1],
                    'name':data[2],
                    'last_name':data[3],
                    'email':data[4],
                    'phone':data[5],
                    'document_type_id':data[6],
                    'document_number':data[7],
                    'password':data[8],
                    'state':data[9],
                    'created_at':data[10],
                    'updated_at':data[11],
                    'deleted_at':data[12],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def edit_user(self, user_id:int, user:User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET role_id = %s, name = %s, last_name = %s, email = %s, phone = %s, document_type_id = %s, document_number = %s, password = %s, state = %s WHERE id =%s", (user.role_id, user.name, user.last_name, user.email, user.phone, user.document_type_id, user.document_number, user.password, user.state, user_id))
            conn.commit()
            conn.close()
            return {"resultado": "User edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_user(self, user_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
       

##user_controller = UserController()