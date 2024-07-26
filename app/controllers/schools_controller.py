import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.schools_model import schools
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class Schools_Controller:
        
    def create_Schools(self, school: schools):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO schools (name, state) VALUES (%s, %s)", (school.name, school.state))
            conn.commit()
            conn.close()
            return {"resultado": "school created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_schools(self, schools_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.id, s.name, pv.name AS state 
                FROM schools s 
                JOIN parameters_values pv ON s.state = pv.id 
                WHERE s.id = %s
            """, (schools_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': int(result[0]),
                    'name': result[1],
                    'state': result[2]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="School not found")
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_schools(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            SELECT s.id, s.name, pv.name AS state, s.created_at, s.updated_at 
            FROM schools s 
            JOIN parameters_values pv ON s.state = pv.id
            WHERE s.deleted_at IS NULL
            """)
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'name': data[1],
                    'state': data[2],
                    'created_at': data[3],
                    'updated_at': data[4]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="School not found")
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_school(self, school_id: int, school: schools):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE schools SET name = %s, state = %s WHERE id = %s
            """, (school.name, school.state, school_id))
            conn.commit()
            return {"resultado": "school edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_parameter_values(self, parameter_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name FROM parameters_values WHERE parameter_id = %s
            """, (parameter_id,))
            result = cursor.fetchall()
            payload = [{'id': data[0], 'name': data[1]} for data in result]
            json_data = jsonable_encoder(payload)
            return {"resultado": json_data}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_school(self, school_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            deleted_at = datetime.now()
            cursor.execute("UPDATE schools SET deleted_at = %s WHERE id = %s", (deleted_at, school_id))
            conn.commit()
            return {"resultado": "Colegio eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        