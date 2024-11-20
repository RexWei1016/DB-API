from db.database import fetch_data, modify_data
from datetime import datetime, date, timedelta
from decimal import Decimal

class DailyMonitorModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO DailyMonitor (m_date, id, weight, height, b_pressure, sleep_dt, sleep_duration, sleep_quality)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (
            data['m_date'], data['id'], data.get('weight'), data.get('height'),
            data.get('b_pressure'), data.get('sleep_dt'),
            data.get('sleep_duration'), data.get('sleep_quality')
        )
        modify_data(query, params)


    @staticmethod
    def get_records_by_user(user_id):
        query = "SELECT * FROM DailyMonitor WHERE ID = %s ORDER BY m_date DESC"
        records = fetch_data(query, (user_id,))

        result = []
        for record in records:
            record_dict = {
                'm_date': record[0],  # 假設 record[0] 是 m_date
                'ID': record[1],      # 假設 record[1] 是 ID
                'weight': record[2],  # 假設 record[2] 是 weight
                'height': record[3],  # 假設 record[3] 是 height
                'b_pressure': record[4], # 假設 record[4] 是 b_pressure
                'sleep_dt': record[5],   # 假設 record[5] 是 sleep_dt
                'sleep_duration': record[6], # 假設 record[6] 是 sleep_duration
                'sleep_quality': record[7]   # 假設 record[7] 是 sleep_quality
            }
            result.append(record_dict)

        # 處理資料中無法序列化為 JSON 的部分
        for record in result:
            # 處理日期類型的欄位
            if isinstance(record['m_date'], (datetime, date)):
                record['m_date'] = record['m_date'].strftime('%Y-%m-%d')  # 格式化日期為字串
            if isinstance(record['sleep_dt'], (datetime, date)):
                record['sleep_dt'] = record['sleep_dt'].strftime('%Y-%m-%d')  # 格式化日期為字串

            # 處理 Decimal 類型欄位
            if isinstance(record['weight'], Decimal):
                record['weight'] = float(record['weight'])  # 轉換 Decimal 為 float
            if isinstance(record['height'], Decimal):
                record['height'] = float(record['height'])  # 轉換 Decimal 為 float

            # 處理 timedelta 類型欄位
            if isinstance(record['sleep_duration'], timedelta):
                # 轉換為秒數
                record['sleep_duration'] = str(record['sleep_duration'])  # 轉換為字串，如 "0:00:05"

        return result
    
    @staticmethod
    def delete_record(user_id, m_date):
        query = "DELETE FROM DailyMonitor WHERE ID = %s AND m_date = %s"
        modify_data(query, (user_id, m_date))
