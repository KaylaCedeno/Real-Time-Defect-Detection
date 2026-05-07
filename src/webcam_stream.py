import cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Placeholder for future defect detection
        text = "Status: analyzing..."
        cv2.putText(frame, text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Real-Time Defect Detection (Prototype)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
