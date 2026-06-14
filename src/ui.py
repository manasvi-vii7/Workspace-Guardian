import cv2

def draw_dashboard(frame, objects, risk, score):

    cv2.rectangle(frame, (10, 10), (400, 180), (0, 0, 0), -1)

    cv2.putText(frame, "Workspace Guardian", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    cv2.putText(frame, f"Risk: {risk}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.putText(frame, f"Focus Score: {score}/100", (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 2)

    cv2.putText(frame, f"Objects: {', '.join(objects)}", (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,200), 1)

    return frame