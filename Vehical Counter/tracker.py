import cv2
import numpy as np
import math

object_rect = [[1,2,3,4]]
center_points = {}
count = 0
id_count = 0
num_vechical = 0

objects_bbs_ids = []

camera = cv2.VideoCapture("video.mp4")
f = 25
w = int(1000 / (f - 1))

object_detector = cv2.createBackgroundSubtractorMOG2(history = None, varThreshold = None)

kernalOp = np.ones((3,3), np.uint8)
kernalOp2 = np.ones((5,5), np.uint8)
kernalC1 = np.ones((11,11), np.uint8)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)
kernal_e = np.ones((5,5), np.uint8)

while True:
    ret, frame = camera.read()
    if not ret: break

    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5)
    height, width, _ =  frame.shape

    roi = frame[50:540 , 200:960]

    fgmask = fgbg.apply(roi)
    ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    mask1 = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp)
    mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernalC1)
    e_img = cv2.erode(mask2, kernal_e)

    contours, _ = cv2.findContours(e_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            detections.append([x, y, w, h])

    for rect in detections:
        x, y, w, h = rect
        cx = (x + x + w) // 2
        cy = (y + y + h) // 2

        same_object_detected = False

        for object_id, pt in center_points.items():
            distance = math.hypot(cx - pt[0], cy - pt[1])

            if distance < 70:
                center_points[object_id] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, object_id])
                same_object_detected = True

                if (y >= 235 and y <= 255) and count != 1:
                    count += 1
                    num_vechical += count

        if same_object_detected is False and count != 1:
            center_points[id_count] = (cx, cy)
            objects_bbs_ids.append([x, y, w, h, id_count])
            id_count += 1
            count += 1
            num_vechical += count

    new_center_points = {}

    for obj_bb_id in objects_bbs_ids:
        _, _, _, _, object_id = obj_bb_id
        center = center_points[object_id]
        new_center_points[object_id] = center

    center_points = new_center_points.copy()
    box_ids = objects_bbs_ids

    count += len(objects_bbs_ids)

    objects_bbs_ids = []
    count = 0

    for box_id in box_ids:
        x, y, w, h, id = box_id
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.rectangle(roi, (10, 10), (75, 75), (0, 255, 0), cv2.FILLED)
    cv2.putText(roi, str(num_vechical), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)

    cv2.imshow("counter", roi)

    if cv2.waitKey(1) == ord('q'): break

camera.release()
cv2.destroyAllWindows()











