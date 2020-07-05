from collections import Counter
from imutils.video import VideoStream
import face_recognition
import pickle
import cv2
import time
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
from database import db_session
from models import Attendance, Student


def face_rec():
    sound = AudioSegment.from_wav('thank_you.wav')              # Play sound
    day = datetime.now().strftime('%A')                         # Today day
    date = datetime.now().strftime('%d-%m-%Y')                  # Today date
    check_IN_Time = datetime.now().strftime('%X')               # Time
    check_OUT_Time = datetime.now().strftime('%X')

    # Current date and time
    now = datetime.now()
    morning = now.replace(hour=8, minute=0, second=0)           # Morning
    evening = now.replace(hour=16, minute=0, second=0)          # Evening
    clock_reset = now.replace(hour=20, minute=0, second=0)      # Clock reset time

    # Load face data from encoding.pickle
    data = pickle.loads(open('encodings.pickle', "rb").read())

    # Set face detection method
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Start camera
    vs = VideoStream(src=0).start()
    time.sleep(1.0)
    # This list stores names of students which checked IN on morning
    # After clock_reset time, it is reset
    stuPresent = []

    # Stores names of detected faces / string length k = 15 -> listed below
    # Cleared after completely filled and returns the maximum detected face
    names_count = []

    # Loop until break condition is satisfied which is keyboard input 'q'
    while True:
        # Start reading frame by frame
        frame = vs.read()
        # Flip image
        frame = cv2.flip(frame, 1)
        # Convert from BGR to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Covert from BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # For drawing rectangle around faces
        rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                          minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
        # cv2 returns boxes
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
        # Encode the captured frame
        encodings = face_recognition.face_encodings(rgb, boxes)

        # Initialize list of names
        names = []
        for encoding in encodings:
            # find matches in encodings
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            # if match is found
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
            names.append(name)

            # initialize a variable to store len of names_count list
            k = len(names_count)

            # fill names_count list till count = k
            if len(names_count) <= 2:
                names_count.append(name)

            # if count of names_list = k
            if k == 2:
                # List all names with their count
                count = Counter(names_count)

                # Return the maximum occurring name
                stu_name = max(count, key=count.get)                    # String

                # if name is unknown skip all if statements
                if not stu_name == 'Unknown':
                    DB = Student.query.filter_by(roll_no=stu_name).first()
                    roll_no = DB.roll_no

                    # Insert data in Attendance DB
                    insert = Attendance(day, date, DB.roll_no, DB.student_name, DB.gender, DB.branch, DB.semester,
                                        check_IN_Time, '', '', '', 'P')
                    db_session.add(insert)
                    db_session.commit()
                    AM = Attendance.query.filter(Attendance.date == date, Attendance.roll_no == roll_no).first()

                    # if current time <= morning
                    if now >= morning:
                        # Insert into db if arrived late or not
                        setattr(AM, 'arrived_on_time', 'Yes')
                        db_session.commit()
                    else:
                        setattr(AM, 'arrived_on_time', 'No')
                        db_session.commit()
                    play(sound)                 # Play Thank you sound
                    time.sleep(2.0)             # Sleep
                    # If student checked IN append roll no to stu Present list
                    if stu_name not in stuPresent:
                        stuPresent.append(stu_name)

                    # If stu name exist in stu present list
                    elif stu_name in stuPresent:
                        # check if current time >= evening
                        if now <= evening:
                            setattr(AM, 'check_out', check_OUT_Time)
                            setattr(AM, 'left_on_time', 'Yes')
                            db_session.commit()
                        else:
                            setattr(AM, 'check_out', check_OUT_Time)
                            setattr(AM, 'left_on_time', 'No')
                            db_session.commit()

                # Clear names list
                names_count.clear()
                # clear morning present list
                if now == clock_reset:
                    # get list of all students who were present on same date and
                    # write absent for those who didn't came
                    if stu_name not in stuPresent:
                        NP = Student.query.filter_by(roll_no=stu_name).all()
                        for n in NP:
                            insert = Attendance(day, date, n.roll_no, n.student_name, n.gender,
                                                n.branch, n.semester, '-', '-', '-', '-', 'A')
                            db_session.add(insert)
                            db_session.commit()
                        stuPresent.clear()

        # For drawing box around face and displaying name
        for ((top, right, bottom, left), name) in zip(boxes, names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

        # Loop break condition
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Cleanup
    cv2.destroyAllWindows()
    vs.stop()
    db_session.remove()

