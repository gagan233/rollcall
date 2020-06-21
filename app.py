import sys
import cv2
import time
from passlib.handlers.sha2_crypt import sha256_crypt

# Database
from database import db_session, init_db
from models import Student, Attendance, Admin

# Face recognition module
from face_recognition_module_SQL import face_rec

# Encode dataset
from encode_faces import encode_faces

# MainWindow UI
from MainWindowUI import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

# For creating database
# init_db()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Error dialog box pop-up
        self.error_dialog = QtWidgets.QErrorMessage()

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.view_cam)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)

        # Tables
        # Student
        self.no_of_rows = db_session.query(Student).count()
        self.ui.stutableWidget.setColumnCount(5)
        # Attendance
        self.no_of_rows_att = db_session.query(Attendance).count()
        self.ui.atentableWidget.setColumnCount(12)

        # Table header
        self.ui.stutableWidget.setHorizontalHeaderLabels(['Name', 'Roll No', 'Gender', 'Branch', 'Semester'])
        self.ui.atentableWidget.setHorizontalHeaderLabels(
            ['Day', 'Date', 'Name', 'Roll No', 'Gender', 'Branch', 'Semester', 'Check IN', 'Check OUT',
             'Arrived Late', 'Left Early', 'Attendance'])

        # BUTTONS
        # Login, Register, Logout buttons
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.registerButton.clicked.connect(self.register)

        # To start face recognition app
        self.ui.faceButton.clicked.connect(self.start_face_rec)

        # Student Database Window Buttons
        self.ui.addRecordButton.clicked.connect(self.addStudent)
        self.ui.deleteRecordButton.clicked.connect(self.deleteStudent)
        self.ui.updateRecordButton.clicked.connect(self.updateStudent)
        self.ui.clearButton.clicked.connect(self.clearAllFields)
        # To start encoding images
        self.ui.encodeButton.clicked.connect(self.encodeImages)
        # For capturing images
        self.ui.openCameraButton.clicked.connect(self.control_timer)
        self.ui.takePhotoButton.clicked.connect(self.click_pic)

        # View Student DB
        self.ui.searchStuButton.clicked.connect(self.searchResult)
        self.ui.refreshStuButton.clicked.connect(self.viewSQLITE)

        # View Attendance DB
        self.ui.refreshAButton.clicked.connect(self.viewAttendance)
        self.ui.searchrollAButton.clicked.connect(self.searchRoll)
        self.ui.searchAButton.clicked.connect(self.searchBranch)

        # Set all buttons to disabled
        self.logged_out()

    # Login START
    def login(self):
        name = self.ui.loginNameEdit.text()
        password = self.ui.loginPAsswordEdit.text()
        admin_name = Admin.query.filter_by(admin_name=name).first()
        if not admin_name:
            self.error_dialog.showMessage('Invalid credentials. Try Again!')
        else:
            admin_password = admin_name.admin_password
            if sha256_crypt.verify(password, admin_password):
                self.logged_in()
                self.ui.label_5.setText(name)
                self.ui.loginNameEdit.clear()
                self.ui.loginPAsswordEdit.clear()
            else:
                self.error_dialog.showMessage('Invalid credentials. Try Again!')

    def logout(self):
        self.ui.loginNameEdit.clear()
        self.ui.loginPAsswordEdit.clear()
        self.ui.label_5.setText('Login!')
        self.logged_out()

    def register(self):
        name = self.ui.loginNameEdit.text()
        pwd = self.ui.loginPAsswordEdit.text()
        password = sha256_crypt.encrypt(str(pwd))
        admin_name = Admin.query.filter_by(admin_name=name).first()
        if admin_name:
            self.error_dialog.showMessage('User name already exists!')
        else:
            insertAd = Admin(name, password)
            db_session.add(insertAd)
            db_session.commit()
            self.error_dialog.showMessage('New user successfully registered!')
            db_session.close()
            self.ui.loginNameEdit.clear()
            self.ui.loginPAsswordEdit.clear()

    def logged_in(self):
        self.ui.loginButton.setEnabled(False)
        self.ui.registerButton.setEnabled(True)
        self.ui.logoutButton.setEnabled(True)
        self.ui.addRecordButton.setEnabled(True)
        self.ui.deleteRecordButton.setEnabled(True)
        self.ui.updateRecordButton.setEnabled(True)
        self.ui.encodeButton.setEnabled(True)
        self.ui.takePhotoButton.setEnabled(True)
        self.ui.searchStuButton.setEnabled(True)
        self.ui.refreshStuButton.setEnabled(True)
        self.ui.refreshAButton.setEnabled(True)
        self.ui.searchrollAButton.setEnabled(True)
        self.ui.searchAButton.setEnabled(True)

    def logged_out(self):
        self.ui.loginButton.setEnabled(True)
        self.ui.registerButton.setEnabled(False)
        self.ui.logoutButton.setEnabled(False)
        self.ui.addRecordButton.setEnabled(False)
        self.ui.deleteRecordButton.setEnabled(False)
        self.ui.updateRecordButton.setEnabled(False)
        self.ui.encodeButton.setEnabled(False)
        self.ui.takePhotoButton.setEnabled(False)
        self.ui.searchStuButton.setEnabled(False)
        self.ui.refreshStuButton.setEnabled(False)
        self.ui.refreshAButton.setEnabled(False)
        self.ui.searchrollAButton.setEnabled(False)
        self.ui.searchAButton.setEnabled(False)
    # Login END

    def start_face_rec(self):
        # for face recognition
        face_rec()

    def encodeImages(self):
        # For encoding images
        self.ui.encodeButton.setDisabled(True)
        encode_faces()
        self.ui.progressBar.setValue(100)
        self.error_dialog.showMessage('Model trained successfully!')
        self.ui.encodeButton.setEnabled(True)

    # Student database START
    # To Add student in Database
    def addStudent(self):
        # UI text fields
        studentName = self.ui.stu_nameEdit.text()
        rollNo = self.ui.roll_noEdit.text()
        gender = self.ui.genderEdit.text()
        branch = self.ui.branchEdit.text()
        semester = self.ui.semesterEdit.text()
        if studentName == '' or rollNo == '' or gender == '' or branch == '' or semester == '':
            self.error_dialog.showMessage('All fields are mandatory!')
        else:
            # Search record
            query_record = Student.query.filter_by(roll_no=rollNo).first()
            # If record not found
            if not query_record:
                insert = Student(rollNo, studentName, gender, branch, semester)
                db_session.add(insert)
                db_session.commit()
                self.error_dialog.showMessage('Record Saved!')
                db_session.close()
            # If record if found
            else:
                self.error_dialog.showMessage('Record already exists!')

    # Delete Record from Student Database
    def deleteStudent(self):
        rollNo = self.ui.roll_noEdit.text()
        if rollNo == '':
            self.error_dialog.showMessage('Please enter Roll no!')
        else:
            query_record = Student.query.filter_by(roll_no=rollNo).first()
            if query_record:
                Student.query.filter_by(roll_no=rollNo).delete(synchronize_session=False)
                db_session.commit()
                self.error_dialog.showMessage('Record deleted!')
                db_session.close()
            else:
                self.error_dialog.showMessage('Record does not exists!')

    # Update student record in student database
    def updateStudent(self):
        studentName = self.ui.stu_nameEdit.text()
        rollNo = self.ui.roll_noEdit.text()
        gender = self.ui.genderEdit.text()
        branch = self.ui.branchEdit.text()
        semester = self.ui.semesterEdit.text()
        if studentName == '' or rollNo == '' or gender == '' or branch == '' or semester == '':
            self.error_dialog.showMessage('All fields are mandatory!')
        else:
            query_record = Student.query.filter_by(roll_no=rollNo).first()
            if query_record:
                Student.query.filter_by(roll_no=rollNo).delete(synchronize_session=False)
                db_session.commit()
                insert = Student(rollNo, studentName, gender, branch, semester)
                db_session.add(insert)
                db_session.commit()
                self.error_dialog.showMessage('Record Updated!')
                db_session.close()
            else:
                self.error_dialog.showMessage('Record does not exists!')

    # Clear all fields in student database window
    def clearAllFields(self):
        self.ui.branchEdit.clear()
        self.ui.genderEdit.clear()
        self.ui.roll_noEdit.clear()
        self.ui.stu_nameEdit.clear()
        self.ui.semesterEdit.clear()

    # Camera code START
    # For capturing images
    def view_cam(self):
        ret, image = self.video_capture.read()
        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(qImg))

    def control_timer(self):
        if not self.timer.isActive():
            self.video_capture = cv2.VideoCapture(0)
            self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
            self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
            self.timer.start(20)
            self.ui.openCameraButton.setText('Close Camera')
        else:
            self.timer.stop()
            self.video_capture.release()
            self.ui.openCameraButton.setText('Start Camera')
            self.ui.imageLabel.setText('Camera will be displayed here.')

    def click_pic(self):
        if self.ui.roll_noEdit.text() == '':
            self.error_dialog.showMessage('Roll No field is empty!')
        else:
            flag, frame = self.video_capture.read()
            roll_no = self.ui.roll_noEdit.text()
            i = 10
            for i in range(i):
                k = str(i)
                path = './dataset/'+str(roll_no)+'/'+k+'.jpg'
                if flag:
                    QtWidgets.QApplication.beep()
                    cv2.imwrite(path, frame)
                    time.sleep(0.2)
                    i += 1
                    if i == 10:
                        break
    # Camera code END
    # Student Database END

    # View student database START
    def viewSQLITE(self):
        self.ui.rollStuEdit.clear()
        self.ui.stutableWidget.setSortingEnabled(False)
        self.ui.stutableWidget.setRowCount(self.no_of_rows)

        datalist = self.query()
        for i in range(self.no_of_rows):
            for j in range(5):
                self.ui.stutableWidget.setItem(i, j, QTableWidgetItem(str(datalist[i][j])))
        self.ui.stutableWidget.setSortingEnabled(True)

    def query(self):
        result = db_session.query(Student).all()
        student_list = []
        for item in result:
            student_list.append([item.student_name, item.roll_no, item.gender, item.branch, item.semester])
        db_session.remove()
        return student_list

    def searchResult(self):
        self.ui.stutableWidget.setSortingEnabled(False)
        roll_no = self.ui.rollStuEdit.text()
        if roll_no == '':
            self.error_dialog.showMessage('Please enter Roll no!')
        else:
            result = db_session.query(Student).filter_by(roll_no=roll_no).first()
            if not result:
                self.error_dialog.showMessage('No record found!')
            else:
                self.ui.stutableWidget.setRowCount(1)
                student = db_session.query(Student).filter_by(roll_no=roll_no).first()
                datalist = [student.student_name, student.roll_no, student.gender, student.branch, student.semester]
                for i in range(1):
                    for j in range(5):
                        self.ui.stutableWidget.setItem(i, j, QTableWidgetItem(str(datalist[j])))
                self.ui.stutableWidget.setSortingEnabled(True)
            db_session.remove()
    # View student database END

    # Attendance Report START
    def viewAttendance(self):
        self.ui.rollAEdit.clear()
        self.ui.branchAEdit.clear()
        self.ui.atentableWidget.setSortingEnabled(False)
        self.ui.atentableWidget.setRowCount(self.no_of_rows_att)

        AttendanceList = self.QueryAttendance()
        for i in range(self.no_of_rows_att):
            for j in range(12):
                self.ui.atentableWidget.setItem(i, j, QTableWidgetItem(str(AttendanceList[i][j])))
        self.ui.atentableWidget.setSortingEnabled(True)

    def QueryAttendance(self):
        result = db_session.query(Attendance).all()
        A_List = []
        for i in result:
            A_List.append([i.day, i.date, i.student_name, i.roll_no, i.gender, i.branch, i.semester, i.check_in,
                           i.check_out, i.arrived_on_time, i.left_on_time, i.attendance])
        db_session.remove()
        return A_List

    def searchRoll(self):
        self.ui.atentableWidget.setSortingEnabled(False)
        roll_no_A = self.ui.rollAEdit.text()
        if roll_no_A == '':
            self.error_dialog.showMessage('Please enter Roll no!')
        else:
            result = db_session.query(Attendance).filter_by(roll_no=roll_no_A).all()
            if not result:
                self.error_dialog.showMessage('No record found!')
            else:
                student_data = []
                for A in result:
                    student_data.append([A.day, A.date, A.student_name, A.roll_no, A.gender, A.branch, A.semester,
                                         A.check_in, A.check_out, A.arrived_on_time, A.left_on_time, A.attendance])
                row_count = db_session.query(Attendance).filter_by(roll_no=roll_no_A).count()
                self.ui.atentableWidget.setRowCount(row_count)
                datalist = student_data
                for i in range(row_count):
                    for j in range(12):
                        self.ui.atentableWidget.setItem(i, j, QTableWidgetItem(str(datalist[i][j])))
                self.ui.atentableWidget.setSortingEnabled(True)
        db_session.remove()

    def searchBranch(self):
        self.ui.atentableWidget.setSortingEnabled(False)
        branch = self.ui.branchAEdit.text()
        if branch == '':
            self.error_dialog.showMessage('Please enter Branch!')
        else:
            result = db_session.query(Attendance).filter_by(branch=branch).all()
            row_count = db_session.query(Attendance).filter_by(branch=branch).count()
            if not result:
                self.error_dialog.showMessage('No record found!')
            else:
                student_data = []
                for A in result:
                    student_data.append([A.day, A.date, A.student_name, A.roll_no, A.gender, A.branch, A.semester,
                                         A.check_in, A.check_out, A.arrived_on_time, A.left_on_time, A.attendance])
                self.ui.atentableWidget.setRowCount(row_count)
                datalist = student_data
                for i in range(row_count):
                    for j in range(12):
                        self.ui.atentableWidget.setItem(i, j, QTableWidgetItem(str(datalist[i][j])))
                self.ui.atentableWidget.setSortingEnabled(True)
        db_session.remove()
    # Attendance Report END


# Launch app
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
