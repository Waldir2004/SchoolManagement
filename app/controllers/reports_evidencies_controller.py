import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.reports_evidencies_model import reports_evidencies
from fastapi.encoders import jsonable_encoder

class Reports_evidencies_Controller:
        
    def create_reports_evidencies(self, reports_evidencies: reports_evidencies):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reports_evidences (type_file_id, uploaded_by) VALUES (%s, %s)", (reports_evidencies.type_file_id, reports_evidencies.uploaded_by))
            conn.commit()
            conn.close()
            return {"resultado": "Evidencies created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_report_evidencies(self, report_evidencies_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reports_evidences WHERE id = %s", (report_evidencies_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'type_file_id':result[1],
                    'uploaded_by':result[3]
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

    def get_reports_evidencies(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reports_evidences")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':int(data[0]),
                    'type_file_id':data[1],
                    'uploaded_by':data[3]
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
    
    def edit_report_evidencies(self, reports_evidencies_id:int, reports:reports_evidencies):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE reports_evidences SET type_file_id = %s, uploaded_by = %s WHERE id =%s", (reports.type_file_id, reports.uploaded_by, reports_evidencies_id))
            conn.commit()
            conn.close()
            return {"resultado": "Report edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_reports_evidencies(self, reports_evidencies_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reports_evidences WHERE id = %s", (reports_evidencies_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Report eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()