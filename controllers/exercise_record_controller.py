from models.exercise_record_model import ExerciseRecordModel
from models.user_model import AppUserModel
from datetime import datetime, date
from decimal import Decimal

class ExerciseRecordController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['exe_date', 'id', 'exe_time']
        if not all(field in data and data[field] for field in required_fields):
            return {"error": "exe_date、id 和 exe_time 為必填欄位"}, 400

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
            # 獲取資料
            records = ExerciseRecordModel.get_records_by_user(user_id)

            # 格式化資料
            result = []
            for record in records:
                record_dict = {
                    'exe_date': record[0],
                    'user_id': record[1],
                    'exercise_type': record[2],
                    'calories': record[3],
                    'exe_time': record[4],
                }
                result.append(record_dict)

            # 處理無法序列化為 JSON 的資料
            for record in result:
                if isinstance(record['exe_date'], (datetime, date)):
                    record['exe_date'] = record['exe_date'].strftime('%Y-%m-%d')

                if isinstance(record['exe_time'], Decimal):
                    record['exe_time'] = float(record['exe_time'])

                if isinstance(record['calories'], Decimal):
                    record['calories'] = float(record['calories'])

            return {"data": result}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_record(user_id, exe_date, exe_time):
        # 檢查 ID 是否存在
        if not AppUserModel.is_account_existing(user_id):
            return {"error": f"User ID {user_id} 不存在"}, 404

        try:
            ExerciseRecordModel.delete_record(user_id, exe_date, exe_time)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
