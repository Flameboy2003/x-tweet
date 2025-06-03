from playwright.sync_api import sync_playwright
from datetime import datetime, timezone
import psycopg2
import schedule
import time

# Database configuration
DB_CONFIG = {
    'host':     'localhost',
    'port':     5432,
    'dbname':   'xtweet_db',
    'user':     'postgres',
    'password': 'root',
}

TABLE_NAME = 'trends_by_hour'

def get_trends(country='india'):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        url = f'https://trends24.in/{country.lower()}/'
        page.goto(url, timeout=120000)
        page.wait_for_selector("ol.trend-card__list", timeout=15000)

        trends = [
            item.inner_text().strip()
            for item in page.query_selector_all("ol.trend-card__list li a")
            if item.inner_text().strip()
        ]
        browser.close()
        return trends

def store_trends_in_db(timestamp, country, trends):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    # create table if not exists
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMPTZ NOT NULL,
            country VARCHAR(100) NOT NULL,
            trends TEXT[] NOT NULL
        )
    """)
    # insert one row
    cur.execute(f"""
        INSERT INTO {TABLE_NAME} (timestamp, country, trends)
        VALUES (%s, %s, %s)
    """, (timestamp, country, trends))
    conn.commit()
    cur.close()
    conn.close()

def fetch_trending_data():
    timestamp = datetime.now(timezone.utc)
    trends = get_trends()
    if not trends:
        print("⚠️  No trends found. Skipping insert.")
        return
    store_trends_in_db(timestamp, "India", trends)
    print(f"✅ Data saved at {timestamp.isoformat()}")
    print("🔎 Recent trends:")
    for i, t in enumerate(trends, 1):
        print(f"  {i}. {t}")

if __name__ == '__main__':
    # run immediately
    fetch_trending_data()

    # schedule every hour
    schedule.every(1).hours.do(fetch_trending_data)
    print("🔁 Scheduler started. Running every 1 hour…")
    while True:
        schedule.run_pending()
        time.sleep(60)