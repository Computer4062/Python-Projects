import numpy as np
import math
import cv2

center_points = {}
objects_bbs_ids = []
id_count = 0
vechical_count = 0
count = 0
person_id = 0


camera = cv2.VideoCapture("video.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history = None, varThreshold = None)

kernelOp = np.ones((3,3), np.uint8)
kernelC1 = np.ones((11,11), np.uint8)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)
kernel_e = np.ones((5,5), np.uint8)

while True:
    ret, frame = camera.read()
    if not ret: break

    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5)
    width, height, _ = frame.shape

    roi = frame[50: 540, 200:960]

    fgmask = fgbg.apply(roi)
    ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    mask1 = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
    mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernelC1)
    e_img = cv2.erode(mask2, kernel_e)

    contours, _ = cv2.findContours(e_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
            detections.append([x, y, w, h])

    for rect in detections:
        x, y, w, h = rect
        cx = (x + x + w) // 2
        cy = (y + y + h) // 2

        same_object_detected = False

        for id, pt in center_points.items():
            distance = math.hypot(cx - pt[0], cy - pt[1])

            if distance < 70:
                center_points[id] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, id])
                same_object_detected = True

                if (y >= 235 and y <= 255) and count != 1:
                    count += 1
                    vechical_count += count

        if same_object_detected is False and count != 1:
            center_points[id_count] = (cx, cy)
            objects_bbs_ids.append([x, y, w, h, id_count])
            count += 1
            vechical_count += 1
            id_count += 1

    new_center_point = {}

    for obj_bb_id in objects_bbs_ids:
        _, _, _, _, object_id = obj_bb_id
        center = center_points[object_id]
        new_center_point[object_id] = center

    center_points = new_center_point.copy()
    box_ids = objects_bbs_ids

    objects_bbs_ids = []
    count = 0

    for box_id in box_ids:
        x, y, w, h, id = box_id

        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(roi, str(id),(x + 15, y + 15), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 4)

    cv2.rectangle(roi, (10, 10), (75, 75), (0, 255, 0), cv2.FILLED)
    cv2.putText(roi, str(vechical_count), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

    cv2.imshow("counter", roi)

    if cv2.waitKey(1) == ord('q'): break

camera.release()
cv2.destroyAllWindows()

