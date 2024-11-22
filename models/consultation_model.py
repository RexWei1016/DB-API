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
    
    @staticmethod
    def get_records_by_coach(cID):
        # 依教練ID取得所有紀錄
        query = '''
            SELECT ID, con_time, content
            FROM Consultation
            WHERE cID = %s
            ORDER BY con_time DESC
        '''
        return fetch_data(query, (cID,))

    @staticmethod
    def update_record_content(cID, user_id, con_time, new_content):
        # 更新指定諮詢紀錄的內容
        query = '''
            UPDATE Consultation
            SET content = %s
            WHERE cID = %s AND ID = %s AND con_time = %s
        '''
        params = (new_content, cID, user_id, con_time)
        modify_data(query, params)
