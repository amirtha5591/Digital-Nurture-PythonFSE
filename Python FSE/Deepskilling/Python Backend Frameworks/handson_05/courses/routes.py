from flask import Blueprint, jsonify, request
from .models import db, Course

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# GET /api/courses/ - Fetch all courses from database
@courses_bp.route('/', methods=['GET'])
def get_all_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses]), 200

# POST /api/courses/ - Insert a new course into the database
@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'code', 'credits', 'department_id']):
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
        
    new_course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id']
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'status': 'success', 'data': new_course.to_dict()}), 201

# GET single course by ID
@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
    return jsonify({'status': 'success', 'data': course.to_dict()}), 200