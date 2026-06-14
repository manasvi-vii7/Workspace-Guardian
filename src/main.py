from ultralytics import YOLO
import cv2
import time

from logic import (compute_risk, focus_score, workspace_state , guardian_verdict, recommendation, risk_reasoning)
from ui import draw_dashboard
from alerts import smart_alert
from logger import log_activity

# Load model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

last_frame_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #  YOLO inference 
    results = model(frame, conf=0.37)

    names = model.names
    detected = []

    for r in results:
        for c in r.boxes.cls:
            detected.append(names[int(c)])

    # Clean duplicates
    detected = list(set(detected))

    # Core intelligence layer
    risk = compute_risk(detected)
    score = focus_score(detected)

    #Feedbacks
    state = workspace_state(detected)
    verdict = guardian_verdict(state)

    # Logging
    log_activity(detected, risk, score,state,verdict)
    
    # Alerts 
    smart_alert(risk)

    # UI overlay
    annotated_frame = results[0].plot()
    annotated_frame = draw_dashboard(annotated_frame, detected, risk, score)

    cv2.imshow("🛡️ Workspace Guardian", annotated_frame)

    # Small CPU-friendly delay 
    if time.time() - last_frame_time < 0.03:
        continue
    last_frame_time = time.time()

    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()