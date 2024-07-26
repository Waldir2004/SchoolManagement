import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.reports_model import reports
from fastapi.encoders import jsonable_encoder

class Reports_Controller:
        
    def create_reports(self, reports: reports):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reports (type_report_id, reporter_id, reported_user_id, description) VALUES (%s, %s, %s, %s)", (reports.type_report_id, reports.reporter_id, reports.reported_user_id, reports.description))
            conn.commit()
            conn.close()
            return {"resultado": "Reports created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_report(self, report_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reports WHERE id = %s", (report_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'type_report_id':result[1],
                    'reporter_id':result[2],
                    'reported_user_id':result[3],
                    'description':result[4]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Report not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_reports(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT reports.id, reports.type_report_id, users.name AS reporter_name, reported_users.name 
                AS reported_user_name, reports.description FROM reports 
                JOIN users AS users ON reports.reporter_id = 
                users.id JOIN users AS reported_users 
                ON reports.reported_user_id 
                = reported_users.id""")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content = {
                    'id': int(data[0]),
                    'type_report_id': data[1],
                    'reporter_id': data[2],
                    'reported_user_id': data[3],
                    'description': data[4]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Reports not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al obtener los reportes")
        finally:
            conn.close()

    def edit_report( self, report_id: int, reports: dict):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE reports 
                SET type_report_id = %s, reporter_id = %s, reported_user_id = %s, description = %s 
                WHERE id = %s
            """, (reports['type_report_id'], reports['reporter_id'], reports['reported_user_id'], reports['description'], report_id))
            conn.commit()
            return {"resultado": "Report edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_reports(self, reports_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reports WHERE id = %s", (reports_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Report eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def search_users(self, name: str):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name FROM users WHERE name LIKE %s", ('%' + name + '%',))
            result = cursor.fetchall()
            conn.close()
            return result
        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()