import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.info_school_model import SchoolInfo
from fastapi.encoders import jsonable_encoder

class InfoSchoolController:
    def create_info_school(self, school: SchoolInfo):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO info_schools (school_id, name, address, phone, email, city_or_municipality_id, director_id, type_id, website) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (school.school_id, school.name, school.address, school.phone, school.email, school.city_or_municipality_id, school.director_id, school.type_id, school.website ))
            conn.commit()
            conn.close()
            return {"resultado": "Informacion del colegio creada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_info_school(self, info_school_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM info_schools WHERE id = %s", (info_school_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'school_id':int(result[1]),
                    'name':result[2],
                    'address':result[3],
                    'phone':result[4],
                    'email':result[5],
                    'city_or_municipality_id':int(result[6]),
                    'director_id':int(result[7]),
                    'type_id':int(result[8]),
                    'website':result[9],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Info school not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_info_schools(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM info_schools")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'school_id':data[1],
                    'name':data[2],
                    'address':data[3],
                    'phone':data[4],
                    'email':data[5],
                    'city_or_municipality_id':data[6],
                    'director_id':data[7],
                    'type_id':data[8],
                    'website':data[9],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Info school not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def edit_info_school(self, info_school_id:int, school:SchoolInfo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE info_schools SET school_id = %s, name = %s, address = %s, phone = %s, email = %s, city_or_municipality_id = %s, director_id = %s, type_id = %s, website = %s WHERE id =%s", (school.school_id, school.name, school.address, school.phone, school.email, school.city_or_municipality_id, school.director_id, school.type_id, school.website, info_school_id))
            conn.commit()
            conn.close()
            return {"resultado": "Info school edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_info_school(self, info_school_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM info_schools WHERE id = %s", (info_school_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Informacion del colegio eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
       