# importing modules
import face_recognition
import cv2

# choice of camera
webcam = cv2.VideoCapture(0)

# loading images
known_image1 = face_recognition.load_image_file("foto1.jpg") # insert name and exstension of desired photo
known_image2 = face_recognition.load_image_file("foto2.jpeg") # insert name and exstension of desired photo
known_image3 = face_recognition.load_image_file("foto3.jpeg") # insert name and exstension of desired photo
known_image4 = face_recognition.load_image_file("foto4.jpeg") # insert name and exstension of desired photo
known_image5 = face_recognition.load_image_file("foto5.jpeg") # insert name and exstension of desired photo

#encoding images
target_encoding1 = face_recognition.face_encodings(known_image1)[0]
target_encoding2 = face_recognition.face_encodings(known_image2)[0]
target_encoding3 = face_recognition.face_encodings(known_image3)[0]
target_encoding4 = face_recognition.face_encodings(known_image4)[0]
target_encoding5 = face_recognition.face_encodings(known_image5)[0]


process_this_frame = True

while True:
    # capture frame
    ret, frame = webcam.read()

    # scaling of the acquired frame
    small_frame = cv2.resize(frame, None, fx=0.20, fy=0.20)
    # conversion colors
    rgb_small_frame = cv2.cvtColor(small_frame, 4)

    if process_this_frame:

        # finding and encoding frames
        face_locations = face_recognition.face_locations(rgb_small_frame)
        frame_encodings = face_recognition.face_encodings(rgb_small_frame)

        # matching fotos with camera frames
        if frame_encodings:
            frame_face_encoding = frame_encodings[0]
            match = face_recognition.compare_faces([target_encoding1], frame_face_encoding)[0]
            if match:
                label = "****" # insert desired name for recognition instead of ****
            else:
                match2 = face_recognition.compare_faces([target_encoding2], frame_face_encoding)[0]
                if match2:
                    label = "****2" # insert desired name for recognition instead of ****2
                else:
                    match3 = face_recognition.compare_faces([target_encoding3], frame_face_encoding)[0]
                    if match3:
                        label = "****3" # insert desired name for recognition instead of ****3
                    else:
                        match4 = face_recognition.compare_faces([target_encoding4], frame_face_encoding)[0]
                        if match4:
                            label = "****4" # insert desired name for recognition instead of ****4
                        else:
                            match5 = face_recognition.compare_faces([target_encoding5], frame_face_encoding)[0]
                            if match5:
                                label = "****5" # insert desired name for recognition instead of ****5
                            else: label = "Unknown"

    process_this_frame = not process_this_frame

    # rectangle creation around the face
    if face_locations:
        top, right, bottom, left = face_locations[0]

        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (0, 255, 0), cv2.FILLED)
        label_font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, label, (left + 6, bottom - 6), label_font, 0.8, (255, 255, 255), 1)
    
    # window name
    cv2.imshow("Face Recognition", frame)

    # stopping capturin loop with "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing and closing all windows
webcam.release()
cv2.destroyAllWindows()