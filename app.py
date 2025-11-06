<<<<<<< Updated upstream
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==================== 数据库模型 ====================
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    major = db.Column(db.String(50))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(50))
    capacity = db.Column(db.Integer, default=30)
    current = db.Column(db.Integer, default=0)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), nullable=False)
    course_id = db.Column(db.String(20), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)

# 创建数据库
with app.app_context():
    db.create_all()

# ==================== 路由 ====================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'student_id': s.student_id, 'name': s.name, 'major': s.major} for s in students])

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{
        'id': c.id,
        'course_id': c.course_id,
        'name': c.name,
        'teacher': c.teacher,
        'capacity': c.capacity,
        'current': c.current,
        'available': c.current < c.capacity
    } for c in courses])

@app.route('/api/enroll', methods=['POST'])
def enroll():
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    
    # 检查是否已选
    existing = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if existing:
        return jsonify({'success': False, 'message': '已选过该课程'})
    
    # 检查课程容量
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
        return jsonify({'success': False, 'message': '课程不存在'})
    if course.current >= course.capacity:
        return jsonify({'success': False, 'message': '课程已满'})
    
    # 选课
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    course.current += 1
    db.session.add(enrollment)
    db.session.commit()
    
    return jsonify({'success': True, 'message': '选课成功'})

@app.route('/api/drop', methods=['POST'])
def drop():
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    
    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
        return jsonify({'success': False, 'message': '未选该课程'})
    
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        course.current = max(0, course.current - 1)
    
    db.session.delete(enrollment)
    db.session.commit()
    
    return jsonify({'success': True, 'message': '退课成功'})

@app.route('/api/my-courses/<student_id>', methods=['GET'])
def get_my_courses(student_id):
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    courses = []
    for e in enrollments:
        course = Course.query.filter_by(course_id=e.course_id).first()
        if course:
            courses.append({
                'course_id': course.course_id,
                'name': course.name,
                'teacher': course.teacher
            })
    return jsonify(courses)

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==================== 数据库模型 ====================
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    major = db.Column(db.String(50))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(50))
    capacity = db.Column(db.Integer, default=30)
    current = db.Column(db.Integer, default=0)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), nullable=False)
    course_id = db.Column(db.String(20), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)

# 创建数据库
with app.app_context():
    db.create_all()

# ==================== 路由 ====================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'student_id': s.student_id, 'name': s.name, 'major': s.major} for s in students])

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{
        'id': c.id,
        'course_id': c.course_id,
        'name': c.name,
        'teacher': c.teacher,
        'capacity': c.capacity,
        'current': c.current,
        'available': c.current < c.capacity
    } for c in courses])

@app.route('/api/enroll', methods=['POST'])
def enroll():
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    
    # 检查是否已选
    existing = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if existing:
        return jsonify({'success': False, 'message': '已选过该课程'})
    
    # 检查课程容量
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
        return jsonify({'success': False, 'message': '课程不存在'})
    if course.current >= course.capacity:
        return jsonify({'success': False, 'message': '课程已满'})
    
    # 选课
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    course.current += 1
    db.session.add(enrollment)
    db.session.commit()
    
    return jsonify({'success': True, 'message': '选课成功'})

@app.route('/api/drop', methods=['POST'])
def drop():
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    
    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
        return jsonify({'success': False, 'message': '未选该课程'})
    
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        course.current = max(0, course.current - 1)
    
    db.session.delete(enrollment)
    db.session.commit()
    
    return jsonify({'success': True, 'message': '退课成功'})

@app.route('/api/my-courses/<student_id>', methods=['GET'])
def get_my_courses(student_id):
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    courses = []
    for e in enrollments:
        course = Course.query.filter_by(course_id=e.course_id).first()
        if course:
            courses.append({
                'course_id': course.course_id,
                'name': course.name,
                'teacher': course.teacher
            })
    return jsonify(courses)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> Stashed changes
