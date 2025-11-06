<<<<<<< Updated upstream
from app import app, db, Student, Course

def init_database():
    """初始化数据库数据"""
    with app.app_context():
        # 清空现有数据
        db.drop_all()
        db.create_all()
        
        # 添加学生
        students = [
            Student(student_id='2021001', name='张三', major='计算机科学'),
            Student(student_id='2021002', name='李四', major='软件工程'),
            Student(student_id='2021003', name='王五', major='数据科学'),
        ]
        
        # 添加课程
        courses = [
            Course(course_id='CS101', name='数据结构', teacher='陈教授', capacity=30),
            Course(course_id='CS102', name='算法设计', teacher='刘老师', capacity=25),
            Course(course_id='CS103', name='操作系统', teacher='王教授', capacity=30),
            Course(course_id='CS104', name='数据库原理', teacher='张老师', capacity=35),
            Course(course_id='CS105', name='计算机网络', teacher='李教授', capacity=28),
        ]
        
        db.session.add_all(students)
        db.session.add_all(courses)
        db.session.commit()
        
        print('✓ 数据库初始化成功！')
        print('\n学生列表：')
        for s in students:
            print(f'  学号: {s.student_id}, 姓名: {s.name}, 专业: {s.major}')
        
        print('\n课程列表：')
        for c in courses:
            print(f'  课程号: {c.course_id}, 课程名: {c.name}, 教师: {c.teacher}')

if __name__ == '__main__':
    init_database()

=======
from app import app, db, Student, Course

def init_database():
    """初始化数据库数据"""
    with app.app_context():
        # 清空现有数据
        db.drop_all()
        db.create_all()
        
        # 添加学生
        students = [
            Student(student_id='2021001', name='张三', major='计算机科学'),
            Student(student_id='2021002', name='李四', major='软件工程'),
            Student(student_id='2021003', name='王五', major='数据科学'),
        ]
        
        # 添加课程
        courses = [
            Course(course_id='CS101', name='数据结构', teacher='陈教授', capacity=30),
            Course(course_id='CS102', name='算法设计', teacher='刘老师', capacity=25),
            Course(course_id='CS103', name='操作系统', teacher='王教授', capacity=30),
            Course(course_id='CS104', name='数据库原理', teacher='张老师', capacity=35),
            Course(course_id='CS105', name='计算机网络', teacher='李教授', capacity=28),
        ]
        
        db.session.add_all(students)
        db.session.add_all(courses)
        db.session.commit()
        
        print('✓ 数据库初始化成功！')
        print('\n学生列表：')
        for s in students:
            print(f'  学号: {s.student_id}, 姓名: {s.name}, 专业: {s.major}')
        
        print('\n课程列表：')
        for c in courses:
            print(f'  课程号: {c.course_id}, 课程名: {c.name}, 教师: {c.teacher}')

if __name__ == '__main__':
    init_database()

>>>>>>> Stashed changes
