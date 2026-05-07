import cv2
def main():
    # Initialize webcam capture (device 0 = default camera)
    cap = cv2.VideoCapture(0)

    # Safety check: ensure the webcam opened correctly
    if not cap.isOpened():
        print("Could not open webcam")
        return

    while True:
        # Read a single frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break # Exit loop if frame capture fails

        # Placeholder for future defect detection
        # Later, this will display model predictions (good/defective)
        text = "Status: analyzing..."
        cv2.putText(frame, text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the raw webcam feed
        cv2.imshow("Real-Time Defect Detection (Prototype)", frame)

        # Press 'q' to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
