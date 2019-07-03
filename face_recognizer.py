#----------------------------------------------
#--- Author         : Group #7
#--- Project        : Digital Image Processign 
#--- Date           : 18th April 2019
#----------------------------------------------

import face_recognition
import cv2
import os

import tkinter as tk
from tkinter import filedialog


# Load some sample pictures and learn how to recognize them.
temp_edson = face_recognition.load_image_file("./database/Edson Trejo/1.png")
edson_trejo_face_encoding_1 = face_recognition.face_encodings(temp_edson)[0]

temp_edson = face_recognition.load_image_file("./database/Edson Trejo/2.png")
edson_trejo_face_encoding_2 = face_recognition.face_encodings(temp_edson)[0]

temp_edson = face_recognition.load_image_file("./database/Edson Trejo/3.png")
edson_trejo_face_encoding_3 = face_recognition.face_encodings(temp_edson)[0]

temp_edson = face_recognition.load_image_file("./database/Edson Trejo/4.png")
edson_trejo_face_encoding_4 = face_recognition.face_encodings(temp_edson)[0]

temp_raul = face_recognition.load_image_file("./database/Raul Martinez/1.png")
raul_martinez_face_encoding_1 = face_recognition.face_encodings(temp_raul)[0]

temp_raul = face_recognition.load_image_file("./database/Raul Martinez/2.png")
raul_martinez_face_encoding_2 = face_recognition.face_encodings(temp_raul)[0]

temp_muniz = face_recognition.load_image_file("./database/Raul Muniz/1.png")
raul_muniz_face_encoding_1 = face_recognition.face_encodings(temp_muniz)[0]

temp_muniz = face_recognition.load_image_file("./database/Raul Muniz/2.png")
raul_muniz_face_encoding_2 = face_recognition.face_encodings(temp_muniz)[0]

known_faces = [
    edson_trejo_face_encoding_1,
    edson_trejo_face_encoding_2,
    edson_trejo_face_encoding_3,
    edson_trejo_face_encoding_4,
    raul_martinez_face_encoding_1,
    raul_martinez_face_encoding_2,
    raul_muniz_face_encoding_1,
    raul_muniz_face_encoding_2
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
#frame_number = 0

current_path = os.getcwd()

#frame = cv2.imread("/home/ahmetozlu/Desktop/edson_work/edson/1.png")
input_image_path = input("please enter the full path of input image: ")
frame = cv2.imread(input_image_path)

# Find all the faces and face encodings in the current frame of video
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

face_names = []
name = None
for face_encoding in face_encodings:
    # See if the face is a match for the known face(s)
    match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

    # If you had more than 2 faces, you could make this logic a lot prettier
    # but I kept it simple for the demo
    if match[0]:
        name = "Edson Trejo"
    if match[1]:
        name = "Edson Trejo"
    if match[2]:
        name = "Edson Trejo"
    if match[3]:
        name = "Edson Trejo"
    elif match[4]:
        name = "Raul Martinez"
    elif match[5]:
        name = "Raul Martinez"
    elif match[6]:
        name = "Raul Martinez"
    elif match[7]:
        name = "Raul Muniz"
    elif match[8]:
        name = "Raul Muniz"
    elif match[9]:
        name = "Raul Muniz"
    else:
        name = "UNKNOWN FACE"

    face_names.append(name)

# Label the results
for (top, right, bottom, left), name in zip(face_locations, face_names):
    if not name:
        continue

    # Draw a box around the face
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Draw a label with a name below the face
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

cv2.imshow('face recognition', frame)
cv2.waitKey(0)

if (name == None):
    print ("***UNKNOWN FACE***")
else:
    for recognized_image_path in os.listdir(current_path + "/database/" + name):
        image_path = current_path + "/database/" + name + "/" + recognized_image_path
        print(image_path)
        face_from_database = cv2.imread(image_path)
        cv2.imshow('face images from database: ' + name, face_from_database)
        cv2.waitKey(0)
