import json
import pyodbc

def lambda_handler(event, context):
    # Extract user information from the event
    user_data = json.loads(event['body'])
    first_name = user_data.get('firstName')
    last_name = user_data.get('lastName')
    
    # Connect to SQL Server database
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=database-1;DATABASE=database-1;UID=admin;PWD=madnan08')
        
        # Insert user information into database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (FirstName, LastName) VALUES (?, ?)", (first_name, last_name))
        conn.commit()
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User information submitted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    finally:
        conn.close()  # Close the database connection

# Your existing Flask application code can go here if needed

