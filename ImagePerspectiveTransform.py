import cv2
import numpy as np


points = []

def mouse_click(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 4:
            perspective_transform()

def perspective_transform():
    global points
    ## 左上開始順時針點擊
    clickedPoints = np.array(points, dtype=np.float32)

    TransformPoints = np.array([
        [0, 0],
        [500, 0],
        [500, 500],
        [0, 500]
    ], dtype=np.float32)

    M = cv2.getPerspectiveTransform(clickedPoints, TransformPoints)
    resultImage = cv2.warpPerspective(image, M, (500, 500))

    cv2.imshow("result", resultImage)
    cv2.imwrite('./ImagePerspectiveTransform/output.jpg', resultImage)


image = cv2.imread('./ImagePerspectiveTransform/Gallery.bmp')
cv2.imshow("Image", image)

cv2.setMouseCallback("Image", mouse_click)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()