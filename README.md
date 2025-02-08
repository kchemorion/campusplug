# CampusPlug

A hyper-localized social and utility app designed exclusively for university students. CampusPlug combines social networking, campus resources, and gamification to create a must-have tool for every student.

## Features

- Campus Feed
- Study Buddy Match
- Campus Deals & Discounts
- Event Hub
- Anonymous Confessions
- Gamification System
- Campus Map & Navigation
- Group Chats & Clubs

## Tech Stack

- Backend: Flask (Python)
- Frontend: React
- Database: PostgreSQL
- Authentication: JWT
- Real-time updates: WebSocket

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
cd frontend
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the development servers:

Backend:
```bash
python run.py
```

Frontend:
```bash
cd frontend
npm start
```

## Project Structure

```
campusplug/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── config.py
│   └── __init__.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── utils/
│   └── package.json
├── requirements.txt
└── README.md
```
