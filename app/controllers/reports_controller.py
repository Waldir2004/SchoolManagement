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
            cursor.execute("SELECT * FROM reports")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':int(data[0]),
                    'type_report_id':data[1],
                    'reporter_id':data[2],
                    'reported_user_id':data[3],
                    'description':data[4]
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
        finally:
            conn.close()
    
    def edit_report(self, reports_id:int, reports:reports):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE reports SET type_report_id = %s, reporter_id = %s, reported_user_id = %s, description = %s WHERE id =%s", (reports.type_report_id, reports.reporter_id, reports.reported_user_id, reports.description, reports_id))
            conn.commit()
            conn.close()
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