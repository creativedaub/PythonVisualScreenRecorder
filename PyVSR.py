from os import system
try:
    from tkinter import *
    from datetime import date, datetime
    from PIL import ImageGrab
    from pyautogui import size
    import cv2, numpy as np, threading, tkinter
except ModuleNotFoundError:
    ls = ['opencv-python', 'pillow', 'tkinter', 'numpy', 'threading', 'pyautogui']
    for any0 in ls:
        cmd = 'pip install ' + any0
        system(cmd)


window = Tk()
window.geometry("500x200+400+170")
window.resizable(False, False)
window.configure(bg="#030818")

desired, a, b = "test", f"{str(date.today()).strip()}", f"{str(datetime.now()).strip()}"
filename = f"{desired} - {a}_{b[11:].replace(':', '')}.mp4"
screensize = size()
recording = threading.Event()


def recorder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30.0
    output = cv2.VideoWriter(filename.strip(), fourcc, fps, screensize)
    print("\nRecording Started")
    recording.set()
    while recording.is_set():
        img = ImageGrab.grab().resize(screensize)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        output.write(frame)
    output.release()   # cv2.destroyWindow('tk')
    print("\nRecording Stopped...")


def start_recording():
    if not recording.is_set():
        threading.Thread(target=recorder).start()


def stop_recording():
    recording.clear()


Label(window, text="PyVS Recorder", fg="white", bg="#030818", font=("Helvetica", 23, "bold")).pack()
start = Button(window, text="Start  Recording", command=start_recording, bd=0, bg="blue", fg="white", font=("Helvetica", 17, "bold"))
start.place(x=150, y=60)
stop = Button(window, text="Stop  Recording", command=stop_recording, bd=0, bg="blue", fg="white", font=("Helvetica", 17, "bold"))
stop.place(x=151, y=110)

window.mainloop()
