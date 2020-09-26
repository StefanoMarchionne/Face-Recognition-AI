# Face-Recognition-AI
[![Python 3.7.9](https://img.shields.io/badge/python-3.7.9-blue.svg)](https://www.python.org/downloads/release/python-379/)

Hi everyone, this project is a simple A.I. for facial recognition via webcam.

## Install dependencies

```bash
pip install -r requirement.txt
```
## Changes to use the project

Replace the name "foto.jpeg" with the relative name and extension of the photo you want to use for recognition and repeat this step for each element in the following code:

```python
# loading images
known_image1 = face_recognition.load_image_file("foto1.jpg") # insert name and exstension of desired photo
known_image2 = face_recognition.load_image_file("foto2.jpeg") # insert name and exstension of desired photo
known_image3 = face_recognition.load_image_file("foto3.jpeg") # insert name and exstension of desired photo
known_image4 = face_recognition.load_image_file("foto4.jpeg") # insert name and exstension of desired photo
known_image5 = face_recognition.load_image_file("foto5.jpeg") # insert name and exstension of desired photo
```
To use more or less photos add or delete the following lines of code.
To add, replacing "N" with a number different from the previous ones:

```python
known_imageN = face_recognition.load_image_file("fotoN.jpg")
```

As another change, in the following part of the code, instead of "****", replace it with the desired name for the person corresponding to the photo previously assigned to the variable "known_imageN" ("N" is the number of the variable to be distinguished from the others as mentioned above).
Then, again in the code part below, if you add photos for recognition, you must also add another part of code, that is another "if / else" for photo, concatenating it with the previous one, before the last 'else:" Unkonown "':

```python
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
```
Here is an example:

```python
...(previous code)
            match4 = face_recognition.compare_faces([target_encoding4], frame_face_encoding)[0]
            if match4:
                label = "****4" # insert desired name for recognition instead of ****4
            else:
                match5 = face_recognition.compare_faces([target_encoding5], frame_face_encoding)[0]
                if match5:
                   label = "****5" # insert desired name for recognition instead of ****5
                #-------------------
                else:
                    matchN = face_recognition.compare_faces([target_encodingN], frame_face_encoding)[0]
                    if matchN:
                       label = "****N" # insert desired name for recognition instead of ****N
                #--------------------
                    else: label = "Unknown"
(next code)...
```

Remembering also to change the number "N" of "target_encodingN" and "matchN" with its corrispectives, in the following lines:

```python
matchN = face_recognition.compare_faces([target_encodingN], frame_face_encoding)[0]
if matchN:
```
## Using the project

To use the project, just run it from the console using:
```bash
python3 face_rec.py
```
or 
```bash
python face_rec.py
```
To stop the process, press 'q'.

## Warnings

**The photos must be in the same folder as the script**
