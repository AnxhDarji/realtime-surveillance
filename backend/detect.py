from ultralytics import YOLO
import cv2
import time
import os

from alert import send_telegram_alert

print("===================================")
print("Realtime Surveillance System Started")
print("Press 'q' to quit")
print("===================================")

# Load YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Create resizable window
cv2.namedWindow("Realtime Surveillance", cv2.WINDOW_NORMAL)

# Check webcam
if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

# Cooldown settings
last_alert_time = 0
cooldown = 20  # seconds

while True:

    # Read frame
    success, frame = cap.read()

    if not success:
        print("Failed to read frame")
        break

    # Run YOLO detection
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    # Current time
    current_time = time.time()

    # Loop through detections
    for box in results[0].boxes:

        # Get class ID
        class_id = int(box.cls[0])

        # Get class name
        class_name = model.names[class_id]

        # Get confidence
        confidence = float(box.conf[0])

        # Detection condition
        if class_name == "person" and confidence > 0.70:

            # Cooldown protection
            if current_time - last_alert_time > cooldown:

                print("⚠ Suspicious person detected!")

                # Time text
                current_time_text = time.strftime("%Y-%m-%d %H:%M:%S")

                # Confidence percentage
                confidence_percent = confidence * 100

                # Alert message
                alert_message = f"""
🚨 SECURITY ALERT 🚨

Detected Object : {class_name}
Confidence Score : {confidence_percent:.1f}%

Detection Time : {current_time_text}

Alert Status : Suspicious Activity Detected
"""

                # Save annotated frame
                image_path = "alert.jpg"

                cv2.imwrite(image_path, annotated_frame)

                try:
                    # Send Telegram alert
                    send_telegram_alert(alert_message, image_path)

                    print("Alert sent successfully!")

                except Exception as e:
                    print("Telegram Error:", e)

                # Wait before deleting image
                time.sleep(2)

                # Delete image safely
                if os.path.exists(image_path):
                    os.remove(image_path)

                # Update cooldown timer
                last_alert_time = current_time

    # Show live webcam feed
    cv2.imshow("Realtime Surveillance", annotated_frame)

    # Quit on q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting system...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()