from db.database import fetch_data, modify_data

class ExerciseRecordModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO ExerciseRecord (exe_date, id, exe_type, calories, exe_time)
            VALUES (%s, %s, %s, %s, %s)
        '''
        params = (
            data['exe_date'],
            data['id'],
            data.get('exe_type'),
            data.get('calories'),
            data['exe_time']
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = "SELECT * FROM ExerciseRecord WHERE id = %s ORDER BY exe_date DESC, exe_time DESC"
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(user_id, exe_date, exe_time):
        query = "DELETE FROM ExerciseRecord WHERE id = %s AND exe_date = %s AND exe_time = %s"
        modify_data(query, (user_id, exe_date, exe_time))
