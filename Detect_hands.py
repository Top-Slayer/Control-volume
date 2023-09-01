import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from cvzone.ClassificationModule import Classifier

# another file
with open("Draw_heart.py", "r") as file:
    draw_heart = file.read()

# Function to calculate tha distance between two points
def distance_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def set_volume(volume):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume_interface.SetMasterVolume(volume / 100.0, None)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

# Variable
key = True

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"    
)
cap = cv2.VideoCapture(0)
detector = HandDetector()

# classifier = Classifier("Model\keras_model.h5","Model\labels.txt")

while True:
    ret, frame = cap.read()
    # flip camera of cv2 library
    frame =  cv2.flip(frame, 1)
    # find the hand and its landmarks
    hands, frame = detector.findHands(frame,True,False)
    prediction, index = classifier.getPrediction(frame)    
#    if(index == 0):
#        exec(draw_heart)
    faces = detect_bounding_box(frame)

    
    print("Detect face: ", faces)
    
    if hands and len(hands) > 0:
        hand = hands[0]
        thumb = hand['lmList'][4] # Thumb finger point
        index = hand['lmList'][8] # Index finger point

        distance = distance_points(thumb[0], thumb[1], index[0], index[1])
        distance = (int(distance) * 100) / 250
        if(distance < 7):
            distance = 0
            # if(key == True):
            #     exec(draw_heart)
            #     key = False
        elif(distance >= 100):
            distance = 100

        cv2.putText(frame, f"Volume: {distance} %", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        set_volume(distance)
        print("Volume: ", distance," %\n")

    # Display camera
    cv2.imshow('Display', frame)
    # Shortkey to Exit
    if cv2.waitKey(1) == ord('q'):
        set_volume(100)
        break
# TheEnd
cap.release()
cv2.destroyAllWindows()

print("ending...")
