from flask import Flask, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Database file path
DB_PATH = 'contacts.db'

def init_db():
    """Initialize the database and create the contacts table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_next_user_id():
    """Generate the next user_id in format uxx (u01, u02, etc.)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get the highest user_id number
    cursor.execute("SELECT user_id FROM contacts ORDER BY CAST(SUBSTR(user_id, 2) AS INTEGER) DESC LIMIT 1")
    result = cursor.fetchone()
    
    if result:
        # Extract the number from the last user_id (e.g., "u05" -> 5)
        last_num = int(result[0][1:])
        next_num = last_num + 1
    else:
        next_num = 1
    
    conn.close()
    return f"u{next_num:02d}"  # Format as u01, u02, etc.

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        # Get data from headers
        name = request.headers.get('name')
        email = request.headers.get('email')
        subject = request.headers.get('subject')
        message = request.headers.get('message')
        
        # Validate required fields
        if not all([name, email, subject, message]):
            missing_fields = []
            if not name: missing_fields.append('name')
            if not email: missing_fields.append('email')
            if not subject: missing_fields.append('subject')
            if not message: missing_fields.append('message')
            
            return jsonify({
                'error': 'Missing required headers',
                'missing_fields': missing_fields
            }), 400
        
        # Generate next user_id
        user_id = get_next_user_id()
        
        # Save to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO contacts (user_id, name, email, subject, message)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, name, email, subject, message))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Contact information saved successfully',
            'user_id': user_id
        }), 201
        
    except sqlite3.Error as e:
        return jsonify({
            'error': 'Database error',
            'details': str(e)
        }), 500
    
    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred',
            'details': str(e)
        }), 500

@app.route('/contacts', methods=['GET'])
def get_contacts():
    """Get all contacts (for testing purposes)"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = cursor.fetchall()
        
        # Convert to list of dictionaries
        contact_list = []
        for contact in contacts:
            contact_list.append({
                'user_id': contact[0],
                'name': contact[1],
                'email': contact[2],
                'subject': contact[3],
                'message': contact[4],
                'created_at': contact[5]
            })
        
        conn.close()
        
        return jsonify({
            'contacts': contact_list,
            'total': len(contact_list)
        }), 200
        
    except sqlite3.Error as e:
        return jsonify({
            'error': 'Database error',
            'details': str(e)
        }), 500

@app.route('/contact/<user_id>', methods=['GET'])
def get_contact(user_id):
    """Get a specific contact by user_id"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contacts WHERE user_id = ?', (user_id,))
        contact = cursor.fetchone()
        
        if contact:
            contact_data = {
                'user_id': contact[0],
                'name': contact[1],
                'email': contact[2],
                'subject': contact[3],
                'message': contact[4],
                'created_at': contact[5]
            }
            return jsonify(contact_data), 200
        else:
            return jsonify({'error': 'Contact not found'}), 404
        
        conn.close()
        
    except sqlite3.Error as e:
        return jsonify({
            'error': 'Database error',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
