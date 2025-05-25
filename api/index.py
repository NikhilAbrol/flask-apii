from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # Enable CORS so Framer or other frontends can access the API

# PostgreSQL connection config
conn = psycopg2.connect(
    dbname='initia_db',
    user='postgres',
    password='POSTdatabase200',
    host='postgres-database.cnoiug6oky9u.eu-north-1.rds.amazonaws.com',
    port='5432'
)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT contact_name, email, contact_pfp FROM crm")
            rows = cursor.fetchall()
        
        # Convert to list of dicts
        data = []
        for row in rows:
            data.append({
                "name": row[0],
                "email": row[1],
                "pfp": row[2]
            })

        return jsonify(data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
