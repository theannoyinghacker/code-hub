import cv2
x=cv2.VideoCapture(0)
x,y,p,q,m,n,e,f=22,23,24,25,15,14,5,13
(a,b,c,d)=17,27,2,9
GPIO.setmode(GPIO.BCM)


imgElon= face_recognition.load_image_file('venv/mutiepie1/Harsh.JPG')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)


while True:
    img=x.read()
    faceloc=face_recognition.face_locations(imgElon)[0]
    encodeElon=face_recognition.face_encodings(imgElon)[0]
    cv2.rectangle(imgElon,(faceloc[3],faceloc[0]),(faceloc[2],faceloc[3]),(255,0,255),2)
    faceloc=face_recognition.face_locations(img)[0]
    encode=face_recognition.face_encodings(img)[0]
    cv2.rectangle(imgElon,(faceloc[3],faceloc[0]),(faceloc[2],faceloc[3]),(255,0,255),2)

    results=face_recognition.recognize_faces(encode,[encodeElon])
    print(results)

    if results == True:
        GPIO.setup(a,GPIO.OUT)
        GPIO.setup (b, GPIO.OUT)
        GPIO.setup (c, GPIO.OUT)
        GPIO.setup (d, GPIO.OUT)
        GPIO.setup (x, GPIO.OUT)
        GPIO.setup (y, GPIO.OUT)
        GPIO.setup (p, GPIO.OUT)
        GPIO.setup (q, GPIO.OUT)
        GPIO.setup (m, GPIO.OUT)
        GPIO.setup (n, GPIO.OUT)
        GPIO.setup (e, GPIO.OUT)
        GPIO.setup(f, GPIO.OUT)

    cv2.imshow("image",img)