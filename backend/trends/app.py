from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Database connection settings
# Database configuration
DB_CONFIG = {
    'host':     'localhost',
    'port':     5432,
    'dbname':   'xtweet_db',
    'user':     'postgres',
    'password': 'root',
}


def get_timestamps():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Query distinct timestamps
    cur.execute("SELECT DISTINCT timestamp FROM trends_by_hour ORDER BY timestamp DESC;")
    timestamps = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [timestamp[0].isoformat() for timestamp in timestamps]

def get_trending_data_by_timestamp(timestamp):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Query trends for a specific timestamp
    cur.execute("""
        SELECT timestamp, country, trends 
        FROM trends_by_hour 
        WHERE timestamp = %s
        LIMIT 1;
    """, (timestamp,))
    
    row = cur.fetchone()
    
    cur.close()
    conn.close()

    if row:
        return {
            'timestamp': row[0].isoformat(),
            'country': row[1],
            'trends': row[2]  # Assuming 'trends' is a list of trend strings
        }
    else:
        return None

@app.route('/api/trends_by_hour/timestamps', methods=['GET'])
def get_timestamps_api():
    timestamps = get_timestamps()
    return jsonify(timestamps)

@app.route('/api/trends_by_hour/<timestamp>', methods=['GET'])
def get_trends_by_timestamp(timestamp):
    trends = get_trending_data_by_timestamp(timestamp)
    if trends:
        return jsonify(trends)
    else:
        return jsonify({'error': 'No data found for this timestamp'}), 404

if __name__ == "__main__":
    app.run(debug=True)
