from connect_mysql import connect_database

def update_member_age(member_id, new_age):
    #Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            #Updating member age
            member_id = member_id
            new_age = new_age
            
            #SQL query
            query = "UPDATE Members SET age = %s WHERE id = %s"

            #Executing the query
            cursor.execute(query, (new_age, member_id))
            conn.commit()
            print("Member and session updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()


update_member_age(1, 32)
