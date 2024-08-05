import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.auth_model import Auth
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
import jwt


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

class AuthController:
        
    def login(self, auth: Auth):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.id, u.email, u.password, u.role_id, r.name AS role_name, u.name, u.last_name, u.phone
                FROM users u
                JOIN roles r ON u.role_id = r.id
                WHERE u.email = %s
            """, (auth.email,))
            user_data = cursor.fetchone()
            conn.close()
            #print(user_data)
            if auth.email==user_data[1] and auth.password == user_data[2]:
                #print("CORRECTO --------------------------------------------")
                user_token={ 
                    "id": user_data[0],
                    "email": user_data[1],
                    "password": user_data[2],
                    "role_id": user_data[3],
                    "role_name": user_data[4],
                    "name": user_data[5],
                    "last_name": user_data[6],
                    "phone": user_data[7]
                    }
                return user_token
            return None
        except mysql.connector.Error as err:
            conn.rollback()
       
    def create_access_token(self,data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        print(encoded_jwt)
        return encoded_jwt

    def validate_token(self,token,  output=False):
        try:
            if(output):
                return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.exceptions.DecodeError:
            return JSONResponse(content={"message":"Token invalido"},status_code=401)
        except jwt.exceptions.ExpiredSignatureError:
            return JSONResponse(content={"message":"Token expirado"},status_code=401)
'''

    def verify_token_expiration(self,token: str):
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            exp = payload.get("exp")
            if exp:
                return datetime.utcnow() > datetime.fromtimestamp(exp)
            return False
        except jwt.PyJWTError:
            return True
    
    def verify_token(self,token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.PyJWTError:
            raise Exception("Invalid token") 
'''
############################
