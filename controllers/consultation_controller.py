from models.consultation_model import ConsultationModel

class ConsultationController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['cID', 'ID', 'con_time']
        if not all(field in data and data[field] for field in required_fields):
            return {"error": "cID、ID 和 con_time 為必填欄位"}, 400

        # 建立新紀錄
        try:
            ConsultationModel.create_record(data)
            return {"message": "紀錄新增成功"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_records(user_id):
        try:
            records = ConsultationModel.get_records_by_user(user_id)
            return {"data": records}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_record(cID, user_id, con_time):
        try:
            ConsultationModel.delete_record(cID, user_id, con_time)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
