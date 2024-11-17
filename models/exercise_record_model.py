from db.database import fetch_data, modify_data

class ExerciseRecordModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO ExerciseRecord (exe_date, ID, exe_type, calories)
            VALUES (%s, %s, %s, %s)
        '''
        params = (
            data['exe_date'], data['ID'], data.get('exe_type'), data.get('calories')
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = "SELECT * FROM ExerciseRecord WHERE ID = %s ORDER BY exe_date DESC"
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(user_id, exe_date):
        query = "DELETE FROM ExerciseRecord WHERE ID = %s AND exe_date = %s"
        modify_data(query, (user_id, exe_date))
