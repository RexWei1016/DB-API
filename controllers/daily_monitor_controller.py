from models.daily_monitor_model import DailyMonitorModel

class DailyMonitorController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['m_date', 'ID']
        if not all(field in data and data[field] for field in required_fields):
            return {"error": "m_date 和 ID 為必填欄位"}, 400

        # 建立新紀錄
        try:
            DailyMonitorModel.create_record(data)
            return {"message": "紀錄新增成功"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_records(user_id):
        try:
            records = DailyMonitorModel.get_records_by_user(user_id)
            return {"data": records}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_record(user_id, m_date):
        try:
            DailyMonitorModel.delete_record(user_id, m_date)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
