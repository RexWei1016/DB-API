from models.exercise_record_model import ExerciseRecordModel

class ExerciseRecordController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['exe_date', 'ID']
        if not all(field in data and data[field] for field in required_fields):
            return {"error": "exe_date 和 ID 為必填欄位"}, 400

        # 建立新紀錄
        try:
            ExerciseRecordModel.create_record(data)
            return {"message": "紀錄新增成功"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_records(user_id):
        try:
            records = ExerciseRecordModel.get_records_by_user(user_id)
            return {"data": records}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_record(user_id, exe_date):
        try:
            ExerciseRecordModel.delete_record(user_id, exe_date)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
