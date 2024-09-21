import numpy as np
import cv2
import pyautogui as py
print("Press 'q'to stop")
outputFile="record.mp4"
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
fps=20.0
size=py.size()
out=cv2.VideoWriter(outputFile,fourcc,fps,size)
try:
    while True:
       img=py.screenshot()
       frame=np.array(img)
       frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
       out.write(frame)
       cv2.imshow("Recording", frame)   
       if cv2.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    print("Recording Stopped !!!")
out.release()
cv2.destroyAllWindows()
print("Recording =Saved as record.mp4 !!!")