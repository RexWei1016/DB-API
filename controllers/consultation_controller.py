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
    def get_records(user_id):
        try:
            records = ConsultationModel.get_records_by_user(user_id)
            if not records:
                return {"message": "No records found"}, 404
            return {"data": records}, 200
        except Exception as e:
            return {"error": f"Failed to fetch records: {str(e)}"}, 500

    @staticmethod
    def delete_record(cID, user_id, con_time):
        try:
            # 確保 timestamp 格式正確
            con_time = datetime.strptime(con_time, '%Y-%m-%d %H:%M:%S')
            ConsultationModel.delete_record(cID, user_id, con_time)
            return {"message": "Record deleted successfully"}, 200
        except ValueError as e:
            return {"error": f"Invalid date format: {str(e)}"}, 400
        except Exception as e:
            return {"error": f"Failed to delete record: {str(e)}"}, 500
