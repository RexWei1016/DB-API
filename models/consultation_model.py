from db.database import fetch_data, modify_data

class ConsultationModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO Consultation (cID, ID, con_time, content)
            VALUES (%s, %s, %s, %s)
        '''
        params = (
            data['cID'],  # 教練帳號
            data['ID'],   # 使用者帳號
            data['con_time'],  # 時間戳
            data.get('content', '')  # 諮詢內容，預設為空
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = '''
            SELECT cID, con_time, content
            FROM Consultation
            WHERE ID = %s
            ORDER BY con_time DESC
        '''
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(cID, user_id, con_time):
        query = '''
            DELETE FROM Consultation
            WHERE cID = %s AND ID = %s AND con_time = %s
        '''
        modify_data(query, (cID, user_id, con_time))
