from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/run-query', methods=['POST'])
def run_query():
    sql = request.json.get('query')
    conn = mysql.connector.connect(
        host="your-db-host",
        user="user",
        password="pwd",
        database="your_db"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"data": rows})
