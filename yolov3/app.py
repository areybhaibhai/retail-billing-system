import cv2
import numpy as np
import pytesseract
from collections import Counter

# Load the pre-trained YOLOv3 model
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Load the class labels
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Set up the camera capture
cap = cv2.VideoCapture("http://192.168.137.91:8080/video")

# Initialize the product list and the total bill amount
product_list = []
total_amount = 0

# Start the camera feed
while True:
    # Read the camera frame
    ret, frame = cap.read()

    # Create a blob from the input image
    blob = cv2.dnn.blobFromImage(
        frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Set the input for the neural network
    net.setInput(blob)

    # Perform object detection
    outputs = net.forward(net.getUnconnectedOutLayersNames())

    # Iterate over the detected objects
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                x = int(center_x - width / 2)
                y = int(center_y - height / 2)
                box_color = (0, 255, 0)
                box_thickness = 2
                text_color = (255, 255, 255)
                text_thickness = 1
                text_scale = 1.0
                font = cv2.FONT_HERSHEY_SIMPLEX

# Draw the bounding box
                cv2.rectangle(frame, (x, y), (x + width, y + height), box_color, box_thickness)

# Add the product name as a label on the bounding box
                label = f'{classes[class_id]}'
                (label_width, label_height), baseline = cv2.getTextSize(label, font, text_scale, text_thickness)
                cv2.rectangle(frame, (x, y - label_height - baseline), (x + label_width, y), box_color, -1)
                cv2.putText(frame, label, (x, y - baseline), font, text_scale, text_color, text_thickness)

# Add the product to the list
                product_list.append(classes[class_id])

    # Display the output image
    cv2.imshow('Retail Product Detection', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera capture
cap.release()
cv2.destroyAllWindows()


def get_product_price(product_name):
    # This is just a placeholder function that returns a random price for each product
    prices = {
        'cola': 2.5,
        'chips': 1.0,
        'chocolate': 3.0,
        'cookies': 2.0
    }
    return prices.get(product_name, 0.0)


# Generate the bill
count = Counter(product_list)
print('Product List:')
for product, quantity in count.items():
    price = get_product_price(product)
    amount = price * quantity
    total_amount += amount
    print(f'{product} - {quantity} x {price} = {amount}')
print(f'Total Amount: {total_amount}')


