import cv2
import sys

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

alive = True

win_name = "Camera Demo"
cv2.namedWindow(win_name , cv2.WINDOW_NORMAL)

source = cv2.VideoCapture(s)


while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    cv2.imshow(win_name , frame)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") :
        alive  = False



source.release()
cv2.destroyWindow(win_name)
