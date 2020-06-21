# models for table creation

from sqlalchemy import Column, Integer, String
from database import Base


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    admin_name = Column(String(256), unique=True)
    admin_email = Column(String(256))
    admin_password = Column(String(256))

    def __init__(self, admin_name=None, admin_email=None, admin_password=None):
        self.admin_name = admin_name
        self.admin_email = admin_email
        self.admin_password = admin_password

    def __repr__(self):
        return '<User %r>' % self.admin_name


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    roll_no = Column(Integer, unique=True)
    student_name = Column(String(256))
    gender = Column(String(6))
    branch = Column(String(10))
    semester = Column(Integer)

    def __init__(self, roll_no=None, student_name=None, gender=None, branch=None, semester=None):
        self.roll_no = roll_no
        self.student_name = student_name
        self.gender = gender
        self.branch = branch
        self.semester = semester

    def __repr__(self):
        return '<User %r>' % self.student_name


# ATTENDANCE TABLE
class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    day = Column(String(10))
    date = Column(String(10))
    roll_no = Column(Integer)
    student_name = Column(String(256))
    gender = Column(String(6))
    branch = Column(String(10))
    semester = Column(Integer)
    check_in = Column(String(15))
    check_out = Column(String(15))
    arrived_on_time = Column(String(3))
    left_on_time = Column(String(3))
    attendance = Column(String(1))

    def __init__(self, day=None, date=None, roll_no=None, student_name=None, gender=None, branch=None, semester=None,
                 check_in=None, check_out=None, arrived_on_time=None, left_on_time=None, attendance=None):
        self.day = day
        self.date = date
        self.roll_no = roll_no
        self.student_name = student_name
        self.gender = gender
        self.branch = branch
        self.semester = semester
        self.check_in = check_in
        self.check_out = check_out
        self.arrived_on_time = arrived_on_time
        self.left_on_time = left_on_time
        self.attendance = attendance

    def __repr__(self):
        return '<User %r>' % self.student_name
