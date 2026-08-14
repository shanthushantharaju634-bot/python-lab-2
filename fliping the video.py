import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Flip state
flip = False


def flip_camera():
    global flip
    flip = not flip


def update_frame():
    ret, frame = cap.read()

    if ret:
        # Flip the frame if flip is ON
        if flip:
            frame = cv2.flip(frame, 1)

        # Convert OpenCV image to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to Tkinter image
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(img)

        # Display webcam
        camera_label.config(image=img)
        camera_label.image = img

    camera_label.after(10, update_frame)


def close_camera():
    cap.release()
    window.destroy()


# Create window
window = tk.Tk()
window.title("Webcam Flip")
window.geometry("800x650")

# Webcam display
camera_label = tk.Label(window)
camera_label.pack(pady=10)

# FLIP button
flip_button = tk.Button(
    window,
    text="FLIP",
    font=("Arial", 16, "bold"),
    command=flip_camera,
    width=12
)
flip_button.pack(pady=10)

# EXIT button
exit_button = tk.Button(
    window,
    text="EXIT",
    font=("Arial", 14),
    command=close_camera,
    width=12
)
exit_button.pack()

# Start webcam
update_frame()

window.mainloop()
