from db.database import fetch_data, modify_data

class DailyMonitorModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO DailyMonitor (m_date, ID, weight, height, b_pressure, sleep_dt, sleep_duration, sleep_quality)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (
            data['m_date'], data['ID'], data.get('weight'), data.get('height'),
            data.get('b_pressure'), data.get('sleep_dt'),
            data.get('sleep_duration'), data.get('sleep_quality')
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = "SELECT * FROM DailyMonitor WHERE ID = %s ORDER BY m_date DESC"
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(user_id, m_date):
        query = "DELETE FROM DailyMonitor WHERE ID = %s AND m_date = %s"
        modify_data(query, (user_id, m_date))
