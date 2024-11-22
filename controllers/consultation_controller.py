from models.consultation_model import ConsultationModel
from datetime import datetime

class ConsultationController:
    @staticmethod
    def create_record(data):
        required_fields = ['cID', 'ID', 'con_time']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return {"error": f"Missing fields: {', '.join(missing_fields)}"}, 400

        # 驗證字段類型
        try:
            data['con_time'] = datetime.strptime(data['con_time'], '%Y-%m-%d %H:%M:%S')  # 檢查 timestamp 格式
        except ValueError as e:
            return {"error": f"Invalid data type: {str(e)}"}, 400

        try:
            ConsultationModel.create_record(data)
            return {"message": "Record created successfully"}, 201
        except Exception as e:
            return {"error": f"Failed to create record: {str(e)}"}, 500

    @staticmethod
    def get_records(user_id: str):
        try:
            records = ConsultationModel.get_records_by_user(user_id)
            if not records:
                return {"message": "No records found"}, 404

            # 將 datetime 物件轉換為字串格式
            formatted_records = []
            for record in records:
                formatted_record = {
                    "cID": record[0],
                    "con_time": record[1].strftime('%Y-%m-%d %H:%M:%S'),  # 將 datetime 轉為字串
                    "content": record[2]
                }
                formatted_records.append(formatted_record)

            return {"data": formatted_records}, 200
        except Exception as e:
            return {"error": f"Failed to fetch records: {str(e)}"}, 500

    @staticmethod
    def delete_record(cID: str, user_id: str, con_time: str):
        try:
            # 確保 timestamp 格式正確
            con_time = datetime.strptime(con_time, '%Y-%m-%d %H:%M:%S')
            ConsultationModel.delete_record(cID, user_id, con_time)
            return {"message": "Record deleted successfully"}, 200
        except ValueError as e:
            return {"error": f"Invalid date format: {str(e)}"}, 400
        except Exception as e:
            return {"error": f"Failed to delete record: {str(e)}"}, 500

    @staticmethod
    def get_records_by_coach(cID: str):
        try:
            records = ConsultationModel.get_records_by_coach(cID)
            if not records:
                return {"message": "No records found"}, 404

            # 將 datetime 物件轉換為字串格式
            formatted_records = []
            for record in records:
                formatted_record = {
                    "ID": record[0],  # 使用者ID
                    "con_time": record[1].strftime('%Y-%m-%d %H:%M:%S'),  # 將 datetime 轉為字串
                    "content": record[2]
                }
                formatted_records.append(formatted_record)

            return {"data": formatted_records}, 200
        except Exception as e:
            return {"error": f"Failed to fetch records: {str(e)}"}, 500

    @staticmethod
    def update_record_content(cID: str, user_id: str, con_time: str, new_content: str):
        try:
            # 確保 timestamp 格式正確
            con_time = datetime.strptime(con_time, '%Y-%m-%d %H:%M:%S')
            print(new_content)
            print(con_time)
            print(cID)
            print(user_id)
            # 更新紀錄
            ConsultationModel.update_record_content(cID, user_id, con_time, new_content)
            
            return {"message": "Record updated successfully"}, 200
        except ValueError as e:
            return {"error": f"Invalid date format: {str(e)}"}, 400
        except Exception as e:
            return {"error": f"Failed to update record: {str(e)}"}, 500
