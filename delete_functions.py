from connect_mysql import connect_database

# Establishing the connection
def delete_workout_session(session_id):
    
    conn = connect_database()
    if conn is not None:
        try:
            cursor  = conn.cursor()

            #Checking if ID exists
            check_query = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_query, (session_id,))
            workout = cursor.fetchone()

            if workout:
                # If workout exists then proceed to delete
                delete_query = "Delete FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_query, (session_id,))
                conn.commit()
                print("Workout deleted successfully.")
            else:
                #If book does not exist then let the user know
                print(f"No workout found with ID: {session_id}")
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
                

delete_workout_session(2)