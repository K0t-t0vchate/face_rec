from tkinter import *
import re
import cv2
import os

clicks = 0


# os.makedirs('face')

def clkbtn():
    global clicks
    clicks += 1
    buttonText.set('Clicks = {}'.format(clicks))
    root.title('Clicker')


root = Tk()
root.title('Graphic program on Python')
root.geometry('400x300+550+250')

buttonText = StringVar()
buttonText.set('Clicks = {}'.format(clicks))
btn = Button(textvariable=buttonText,
             text='GO',
             padx='20',
             pady='8',
             command=clkbtn)

btn.pack()
root.mainloop()

cam = cv2.VideoCapture(0)  # создает камеру
cam.set(3, 640)  # ее размеры
cam.set(4, 480)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # распознователь лица

face_id = input('\n введи юзер айди ')

print('\n Установка распознования. Смотрите четко в камеру и ожидайте..')
count = 0

while (True):

    ret, img = cam.read()  # сохранение кадров в эти переменные
    img = cv2.flip(img, 1)  # зеркалит
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # перекрас в серые оттенки
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:  # размер квадрата фото
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # передача характеристик кадра
        count += 1

        cv2.imwrite('face/user.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y + h, x:x + w])  # запись юзера

        cv2.imshow('image', img)  # включает камеру

    k = cv2.waitKey(100) & 0xff  # ожидание нажатия
    if k == 27:  # номер клавиши
        break
    elif count >= 10:  # кол-во кадров
        break

print('\n Выход из программы и зачистка данных')
cam.release()  # очищение окна
cv2.destroyAllWindows()  #
