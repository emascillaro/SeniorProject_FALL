# YOLO object detection
import cv2 as cv
import numpy as np
import time
import Capture_Image

from Speech_Recognition import understood_speech

if understood_speech == 1:

    from Speech_Recognition import noun_list

    #print("read image file")
    # Read image file
    img = cv.imread('Capture_Image.jpg')
    #img = cv.resize(img0, (img0.shape[0] // 8, img0.shape[1] // 8)) # Resize large images proportionally (1/8)
    #print("show image")
    #cv.imshow('window',  img)
    #cv.waitKey(0)

    #print("Load names of classes and get random colors")
    # Load names of classes and get random colors 
    classes = open('coco.names').read().strip().split('\n')
    np.random.seed(42)
    colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')

    #print("Give the configuration and weight files for the model and load the network")
    # Give the configuration and weight files for the model and load the network
    net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    # net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

    #print("determine the output layer")
    # determine the output layer
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    #print("Construct a blob from the image")
    # construct a blob from the image
    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
    r = blob[0, 0, :, :]

    #print("show the blob")
    # Show the blob
    #cv.imshow('blob', r)
    text = f'Blob shape={blob.shape}'
    #cv.displayOverlay('blob', text)
    #cv.waitKey(1)

    net.setInput(blob)
    t0 = time.time()
    outputs = net.forward(ln)
    t = time.time()
    #print('time=', t-t0)

    #print(len(outputs))
    #for out in outputs:
    #    print(out.shape)

    #print("create trackbar for confidence levels on blob")
    # Create trackbar for confidence levels on blob
    def trackbar2(x):
        confidence = x/100
        r = r0.copy()
        for output in np.vstack(outputs):
            if output[4] > confidence:
                x, y, w, h = output[:4]
                p0 = int((x-w/2)*416), int((y-h/2)*416)
                p1 = int((x+w/2)*416), int((y+h/2)*416)
                cv.rectangle(r, p0, p1, 1, 1)
        #cv.imshow('blob', r)
        text = f'Bbox confidence={confidence}'
        #cv.displayOverlay('blob', text)

    r0 = blob[0, 0, :, :]
    r = r0.copy()
    #cv.imshow('blob', r)
    #cv.createTrackbar('confidence', 'blob', 50, 101, trackbar2)
    #trackbar2(50)

    boxes = []
    confidences = []
    classIDs = []
    h, w = img.shape[:2]

    #print("Detect Objects")
    # Detect objects
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.5: #Set confidence level to create bounding box
                box = detection[:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                box = [x, y, int(width), int(height)]
                boxes.append(box)
                confidences.append(float(confidence))
                classIDs.append(classID)

    indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)



    #print("Draw bounding boxes")
    # Draw bounding boxes
    items = []
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            
            # Removes confdience from text
            text_short = text.rsplit(':', 1)[0]

            # Fills list with all items detected in the image
            items.append(text_short)

    print("items: ", items)

    for noun in noun_list:
        if items.count(noun) > 1:
            print(noun, " is in the area more than once.")
        elif items.count(noun) == 1:
            print(noun, " is in the area once.")
        else:
            print(noun, "is not in the area")

    '''
    # Show image with bounding boxes
    cv.imshow('window', img)
    print("new img")
    #print(text)
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''