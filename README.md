# 🐦 X-Tweet: Twitter Trend Analysis Platform

X-Tweet is a web application that analyzes Twitter trends in real-time using NLP and ML techniques like sentiment analysis, topic modeling, anomaly detection, and more.

---

## 🚀 Features

- 🔍 Live Tweet Feed (via Twitter API v2)
- 📊 Sentiment Analysis using VADER
- 🧠 Topic Modeling using BERTopic
- ⚠️ Anomaly Detection on tweet patterns
- 👥 Bot vs. Human Classification
- 📈 Comparative Trend Analysis
- 🌟 Influencer Impact Study
- 📁 CSV Export of results

---

## 🛠 Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | Vue 3 + Tailwind CSS |
| Backend  | Django REST Framework |
| Database | PostgreSQL |
| ML/NLP   | VADER, BERTopic |
| Charts   | Chart.js |

---

## 📦 Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/x-tweet.git
cd x-tweet

2. Backend Setup (Django)

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

3. Frontend Setup (Vue)

cd ../frontend
npm install
npm run dev

Inside your setting.py 
TWITTER_BEARER_TOKEN=your_actual_twitter_bearer_token_here
