# filename: recognize_faces_in_pictures.py
# -*- coding:utf-8 -*-
# import face_recognition module, using command : pip install face_recognition
import face_recognition
import os
import numpy as np
from PIL import Image


# Now,the point is that we can process many jpg file, in order to replace the below code


def ResizeImage(filein, fileout, width=400, height=300):
    # """按照图片长宽比进行分割"""
    im = Image.open(filein)
    width = float(width)
    height = float(height)
    (x, y) = im.size
    if width > height:
        region = (0, int((y - (y * (height / width))) / 2), x, int((y + (y * (height / width))) / 2))
    elif width < height:
        region = (int((x - (x * (width / height))) / 2), 0, int((x + (x * (width / height))) / 2), y)
    else:
        region = (0, 0, x, y)

        # 裁切图片
    crop_img = im.crop(region)
    # 保存裁切后的图片
    crop_img.save(fileout)


def load_jpg(dirName):
    label = []
    img_coding = []
    for parent, dirnames, filenames in os.walk(dirName):
        index = 0
        print filenames
        for filename in filenames:
            print parent + '/' + filename
            # adjust the pciture's size
            # img_resize = Image.open(parent + '/' + filename)

            ResizeImage(parent + '/' + filename, parent + '/' + filename)

            img = face_recognition.load_image_file(parent + '/' + filename)
            coding = face_recognition.face_encodings(img)[0]

            img_coding.append(coding)


            label.append(parent + '/' + filename)
            index += 1
            # print 'img_coding', img_coding
    return img_coding, label

if __name__ == "__main__":
    # load the jpg file into numpy array
    # gutianle_image = face_recognition.load_image_file("/home/liuhh/Downloads/known/guzai.jpg")
    # liuhh_image = face_recognition.load_image_file("/home/liuhh/Downloads/known/liuhh.JPG")
    # unknown_image = face_recognition.load_image_file("/home/liuhh/Downloads/unknown/liuhh.jpg")
    unknown_image = face_recognition.load_image_file("/usr/local/face_recognition_package/faceImg/machine/001.jpeg")

    # get the facial coding
    # return a list of coding
    # index = 0
    # gutianle_face_encoding = face_recognition.face_encodings(gutianle_image)[0]
    # liuhh_face_encoding = face_recognition.face_encodings(liuhh_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    # print 'unknown face',unknown_face_encoding

    # known_faces = [
    #    gutianle_face_encoding,
    #    liuhh_face_encoding
    # ]

    # result is True/False
    # known_faces, label = load_jpg('/home/liuhh/Downloads/known')
    known_faces, label = load_jpg('/usr/local/face_recognition_package/faceImg/livephoto')

    results = face_recognition.compare_faces(known_faces, unknown_face_encoding, tolerance=0.48)
    distance = face_recognition.face_distance(known_faces, unknown_face_encoding)

    print("never met before?{}".format(not True in results))
    print("the distance is {}".format(distance))