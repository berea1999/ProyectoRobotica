import cv2
import numpy as np

CONFIDENCE = 0.5
THRESHOLD = 0.4

LABELS = open("labels.txt").read().strip().split("\n")

# ------------------------ ESCOLLIR MODEL -------------------------------------
m=676
resolution=676*640/3264
resolution=133
distancia=450
baseDir = "YOLOv3"
#baseDir = "tinyYOLOv3"

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

net = cv2.dnn.readNetFromDarknet(baseDir + "/yolov3.cfg", baseDir + "/yolov3.weights")
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if ret:
		

        (H, W) = frame.shape[:2]
		# START RECOGNITION #
        print(H)
        print(W)
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        layerOutputs = net.forward(ln)

		# initialize our lists of detected bounding boxes, confidences, and
		# class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

		# CREAR BOXES AL VOLTANT DE DETECCIONS #

		# loop over each of the layer outputs
        for output in layerOutputs:
			# loop over each of the detections
            for detection in output:
				# extract the class ID and confidence (i.e., probability) of
				# the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
				# filter out weak predictions by ensuring the detected
				# probability is greater than the minimum probability
                if confidence > CONFIDENCE:
					# scale the bounding box coordinates back relative to the
					# size of the image, keeping in mind that YOLO actually
					# returns the center (x, y)-coordinates of the bounding
					# box followed by the boxes' width and height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
					# use the center (x, y)-coordinates to derive the top and
					# and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
					# update our list of bounding box coordinates, confidences,
					# and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)

		# ensure at least one detection exists
        if len(idxs) > 0:
			# loop over the indexes we are keeping
            for i in idxs.flatten():
				# extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
				# draw a bounding box rectangle and label on the image
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                object_image_sensor=h/resolution
                object_size=(distancia*object_image_sensor/4.15)/10
                text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                print("object----------------------------------")
                print(text)
                print('object real size cm-----------------------------')
                print(object_size)
                if object_size>=17,5:
                    accion='seguir buscando';
                elif (object_size<17,5) and (object_size>=10):
                    accion='empujar';
                elif (object_size<10)and(object_size>=1,5):
                    accion='coger';
                    if distancia>150:
                        accion='acercarse';
                else:
                    accion='aplastar';
                print(accion)
                texto = text + ' ' + str(round(object_size,2))+'cm'+' '+accion;
                cv2.putText(frame, texto, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
                               
        cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cam.release()
        break
