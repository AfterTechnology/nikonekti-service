from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from pymongo import MongoClient


name = "service"
bp = Blueprint(name, __name__, template_folder="templates", static_folder="static", static_url_path="/", url_prefix="/")

@bp.route('/reports')
def reports():
    template_name = '/root/reports.html'
    render_template(template_name)



# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['services_db']
messages_collection = db['messages']

@bp.route('/submit', methods=['POST'])
def submit_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Validate the data (optional)
    if not name or not email or not message:
        return jsonify({'error': 'Please fill in all required fields.'}), 400

    # Insert the message into the database
    messages_collection.insert_one({
        'name': name,
        'email': email,
        'message': message
    })

    return jsonify({'message': 'Message submitted successfully'})