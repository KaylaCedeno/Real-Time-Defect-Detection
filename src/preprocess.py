import cv2

def preprocess(frame):
    """
    Basic preprocessing pipeline for defect detection.
    Add later: thresholding, contour detection, or ML-based preprocessing.
    """

    # Convert the frame to grayscale (simplifies processing)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and smooth the image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Return the processed frame (still grayscale)
    return blurred
