from ultralytics import YOLO
import cv2

print("===================================")
print("Realtime Surveillance System Started")
print("Press 'q' to quit")
print("===================================")

# Load YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Open default webcam
cap = cv2.VideoCapture(0)

# Check webcam
if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

while True:
    # Read frame
    success, frame = cap.read()

    if not success:
        print("Failed to read frame")
        break

    # Run YOLO detection
    results = model(frame)

    # Draw detections on frame
    annotated_frame = results[0].plot()

    # Display frame
    cv2.imshow("Realtime Surveillance", annotated_frame)

    # Quit on pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting system...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()