import cv2
import numpy as np


def track_pitch_line(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or unable to load.")
        return
    
    # Convert to grayscale (Canny works on single channel)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)
    
    # Apply Canny edge detector
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    
    # Use Hough Line Transform to detect lines
    # rho and theta are resolution parameters; threshold is minimum votes to detect a line
    lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
    
    # If lines were detected
    if lines is not None:
        # Take the first line (strongest)
        rho, theta = lines[0][0]
        
        # Convert polar coordinates (rho, theta) to endpoints for drawing
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        
        # Calculate two points on the line far enough to draw across the image
        line_length = 1000  # length of the line to draw
        x1 = int(x0 + line_length * (-b))
        y1 = int(y0 + line_length * (a))
        x2 = int(x0 - line_length * (-b))
        y2 = int(y0 - line_length * (a))
        
        # Draw the line on the original image (red color, thickness 3)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
    else:
        print("No lines detected.")
    
    # Show the results
    cv2.imshow('Canny Edges', edges)
    cv2.imshow('Tracked Pitch Line', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter path to the football pitch image: ")
    track_pitch_line(image_path)
