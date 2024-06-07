from connect_mysql import connect_database

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor  = conn.cursor()
            query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"

            cursor.execute(query, (start_age, end_age))
            print(f"Members between age {start_age} and {end_age}:")
            for member in cursor.fetchall():
                print(member)
        
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()


get_members_in_age_range(25, 30)
            
        