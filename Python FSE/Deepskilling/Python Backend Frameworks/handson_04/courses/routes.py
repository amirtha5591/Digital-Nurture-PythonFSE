from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# In-memory temporary list acting as our mock database for now
MOCK_COURSES = []

@courses_bp.route('/', methods=['GET'])
def get_all_courses():
    return jsonify(MOCK_COURSES), 200

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Missing payload data'}), 400
        
    required = ['name', 'code', 'credits']
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({'status': 'error', 'message': f"Missing fields: {', '.join(missing)}"}), 400

    new_course = {
        'id': len(MOCK_COURSES) + 1,
        'name': data['name'],
        'code': data['code'],
        'credits': data['credits']
    }
    MOCK_COURSES.append(new_course)
    return jsonify({'status': 'success', 'data': new_course}), 201

@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = next((c for c in MOCK_COURSES if c['id'] == course_id), None)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
    return jsonify({'status': 'success', 'data': course}), 200

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = next((c for c in MOCK_COURSES if c['id'] == course_id), None)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
        
    data = request.get_json() or {}
    course['name'] = data.get('name', course['name'])
    course['code'] = data.get('code', course['code'])
    course['credits'] = data.get('credits', course['credits'])
    return jsonify({'status': 'success', 'data': course}), 200

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    global MOCK_COURSES
    course = next((c for c in MOCK_COURSES if c['id'] == course_id), None)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
        
    MOCK_COURSES = [c for c in MOCK_COURSES if c['id'] != course_id]
    return jsonify({'status': 'success', 'message': 'Course deleted successfully'}), 200

@courses_bp.app_errorhandler(404)
def handle_not_found(e):
    return jsonify({'status': 'error', 'message': 'Resource URL route not found'}), 404