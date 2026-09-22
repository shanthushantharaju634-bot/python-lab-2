import cv2
import numpy as np

# Variables to track mouse state and drawing coordinates
drawing = False # True if mouse is pressed
ix, iy = -1, -1
canvas = None


def draw_line(event, x, y, flags, param):
  global ix, iy, drawing, canvas

  # Mouse left-click down: Start drawing
  if event == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    ix, iy = x, y

  # Mouse move: Draw line segment if mouse button is held down
  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing:
      cv2.line(canvas, (ix, iy), (x, y), (0, 0, 805), 5)
      ix, iy = x, y

  # Mouse left-click up: Stop drawing
  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False
    cv2.line(canvas, (ix, iy), (x, y), (0, 0, 180), 8)


# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a window and attach the mouse callback function
cv2.namedWindow('Webcam Drawing')
cv2.setMouseCallback('Webcam Drawing', draw_line)

while True:
  ret, frame = cap.read()
  if not ret:
    break

  # Mirror the frame horizontally for natural movement
  frame = cv2.flip(frame, 1)

  # Initialize canvas size once frame size is known
  if canvas is None:
    canvas = np.zeros_like(frame)

  # Overlay the drawn lines onto the webcam frame
  combined_frame = cv2.add(frame, canvas)

  cv2.imshow('Webcam Drawing', combined_frame)

  key = cv2.waitKey(1) & 0xFF
  # Press 'c' to clear the drawing canvas
  if key == ord('c'):
    canvas = np.zeros_like(frame)
  # Press 'q' to quit
  elif key == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()