from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId


name = "index"
bp = Blueprint(name, __name__, static_folder="static", template_folder="templates", static_url_path="/", url_prefix="/")

@bp.route("/", methods=["GET"])
def index_root():
    
    template_name = "/root/index.html"
    return render_template(
        template_name
    )

@bp.route("/frequent")
def frequent():
    
    template_name = "/root/frequent.html"
    return render_template(
        template_name
    )

@bp.route("/support", methods=["GET"])
def support():
     template_name = '/root/support.html'

     return render_template(
          template_name
     )

@bp.route("/create", methods=["GET"])
def create():
     template_name = '/root/create.html'

     return render_template(
          template_name
     )

@bp.route("/reports", methods=["GET"])
def reports():
     template_name = '/root/reports.html'

     return render_template(
          template_name
     )
# Database Setup
client = MongoClient('mongodb://localhost:27017/')
db = client.customer_service_db
complaints = db.complaints

@bp.route('/index')
def index():
    return render_template('/root/contact.html')

@bp.route('/response')
def response():
    return render_template('/root/response.html')

@bp.route('/index.submit', methods=['POST'])
def submit_complaint():
    data = request.form
    print(data)

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Store in MongoDB
    complaints.insert_one({
        'name': name,
        'email': email,
        'message': message,
        'resolved': False
    })
    
    return redirect(url_for('index.response'))

@bp.route('/admin')
def admin_dashboard():
    # Fetch all complaints from the database
    all_complaints = complaints.find()
    return render_template('/root/admin.html', complaints=all_complaints)

@bp.route('/resolve/<id>', methods=['POST'])
def resolve_complaint(id):
    # Mark complaint as resolved
    complaints.update_one({'_id': ObjectId(id)}, {'$set': {'resolved': True}})
    return redirect(url_for('index.admin_dashboard'))

@bp.route('/delete/<id>', methods=['POST'])
def delete_complaint(id):
    # Delete complaint from the database
    complaints.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index.admin_dashboard'))


