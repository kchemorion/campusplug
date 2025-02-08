from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Secret key for JWT
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production

# Mock user database
users = {
    "demo@example.com": {
        "password": "demo123",
        "username": "MariaGarcia",
        "points": 1250,
        "level": "Fiesta Master",
        "year": 3,
        "university": "Universidad de Madrid",
        "major": "Computer Science"
    }
}

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = users.get(email)
    if user and user['password'] == password:
        token = jwt.encode({
            'email': email,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, app.config['SECRET_KEY'])
        
        return jsonify({
            'token': token,
            'user': {
                'email': email,
                'username': user['username'],
                'points': user['points'],
                'level': user['level']
            }
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    
    if email in users:
        return jsonify({'message': 'Email already registered'}), 400
    
    users[email] = {
        'password': data.get('password'),
        'username': data.get('username'),
        'points': 0,
        'level': 'Novice',
        'year': data.get('year'),
        'university': data.get('university'),
        'major': data.get('major')
    }
    
    token = jwt.encode({
        'email': email,
        'exp': datetime.utcnow() + timedelta(days=1)
    }, app.config['SECRET_KEY'])
    
    return jsonify({
        'token': token,
        'user': {
            'email': email,
            'username': users[email]['username'],
            'points': users[email]['points'],
            'level': users[email]['level']
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
