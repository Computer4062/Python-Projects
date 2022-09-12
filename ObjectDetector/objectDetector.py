import cv2
import matplotlib.pyplot as plt

print("working")

config_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "frozen_inference_graph.pb"

model = cv2.dnn_DetectionModel(frozen_model, config_file)

Labels = []
file = 'Labels.txt'

with open(file,'rt') as fpt:
    Labels = fpt.read() .rstrip('\n') .split('\n')

model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)

camera = cv2.VideoCapture(0)

font_size = 3
font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, frame = camera.read()
    classIndex, confidence, bbox = model.detect(frame,confThreshold=0.55)
    
    if (len(classIndex) != 0):
        for classInd, conf, box in zip(classIndex.flatten(), confidence.flatten(), bbox):
            if classInd<80:
                cv2.rectangle(frame,box,(0,255,0), 2 )
                cv2.putText(frame, Labels[classInd-1],(box[0]+10,box[1]+40), font, font_size,color=( 255, 0, 0), thickness=2)
                
    cv2.imshow("ObjectDetector", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
        
                
        




    
