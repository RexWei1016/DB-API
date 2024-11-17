from db.database import fetch_data, modify_data

class ConsultationModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO Consultation (cID, ID, con_time, content)
            VALUES (%s, %s, %s, %s)
        '''
        params = (
            data['cID'], data['ID'], data['con_time'], data.get('content')
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = "SELECT * FROM Consultation WHERE ID = %s ORDER BY con_time DESC"
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(cID, user_id, con_time):
        query = "DELETE FROM Consultation WHERE cID = %s AND ID = %s AND con_time = %s"
        modify_data(query, (cID, user_id, con_time))
