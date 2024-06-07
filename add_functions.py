from connect_mysql import connect_database

def add_member(id, name, age, trainer_id):
    query = "INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, name, age, trainer_id))

def add_workout_session(member_id, session_date, duration_minutes, calories_burned):
    query = "INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (member_id, session_date, duration_minutes, calories_burned))


#Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #Add Member
        add_member(2, "Ricky Patel", 30, 1)
        add_member(3, "Ron", 26, 3)
        add_member(4, "Rick", 32, 5)



        
        #Add Workout Session
        add_workout_session(1, "2024-06-26", "60 min", "1000 cals burned")

        conn.commit()
        print("Member and session logged successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()