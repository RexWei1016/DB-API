from models.exercise_record_model import ExerciseRecordModel
from models.user_model import AppUserModel

class ExerciseRecordController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['exe_date', 'id']
        if not all(field in data and data[field] for field in required_fields):
            return {"error": "exe_date 和 ID 為必填欄位"}, 400

        # 檢查 ID 是否存在
        if not AppUserModel.is_account_existing(data['id']):
            return {"error": f"User ID {data['id']} 不存在"}, 404

        # 處理其他可選字段
        optional_fields = ['exe_type', 'calories']
        sanitized_data = {field: data.get(field) for field in required_fields + optional_fields}

        # 建立新紀錄
        try:
            ExerciseRecordModel.create_record(sanitized_data)
            return {"message": "紀錄新增成功"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_records(user_id):
        # 檢查 ID 是否存在
        if not AppUserModel.is_account_existing(user_id):
            return {"error": f"User ID {user_id} 不存在"}, 404

        try:
            records = ExerciseRecordModel.get_records_by_user(user_id)
            return {"data": records}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_record(user_id, exe_date):
        # 檢查 ID 是否存在
        if not AppUserModel.is_account_existing(user_id):
            return {"error": f"User ID {user_id} 不存在"}, 404

        try:
            ExerciseRecordModel.delete_record(user_id, exe_date)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
