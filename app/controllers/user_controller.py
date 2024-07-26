import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder
from datetime import datetime

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
        
    
    def get_dictypedocument(self):
        try:    
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name FROM parameters_values WHERE parameter_id = 1")
            schools = cursor.fetchall() 
    
            conn.close()
    
            return schools
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()

    def get_dicrol(self):
        try:    
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name FROM roles")
            schools = cursor.fetchall() 
    
            conn.close()
    
            return schools
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
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
            cursor.execute("""SELECT u.id, u.name, u.last_name, u.email, u.phone, u.document_number, u.password, u.state, dt.name 
                            AS document_type_name, r.name AS role_name, u.created_at, u.updated_at FROM users u 
                            JOIN parameters_values dt ON u.document_type_id = dt.id JOIN roles r ON u.role_id = r.id 
                            WHERE u.deleted_at IS NULL;""")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'name':data[1],
                    'last_name':data[2],
                    'email':data[3],
                    'phone':data[4],
                    'document_number':data[5],
                    'password':data[6],
                    'state':data[7],
                    'document_type_name':data[8],
                    'role_name':data[9],
                    'created_at':data[10],
                    'updated_at':data[11]
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
            deleted_at = datetime.now()
            cursor.execute("UPDATE users SET deleted_at = %s WHERE id = %s", (deleted_at, user_id))
            conn.commit()
            return {"resultado": "Usuario eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  

##user_controller = UserController()