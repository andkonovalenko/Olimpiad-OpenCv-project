import cv2
import numpy as np


def save_video_result():
    filename = str(input("Enter path video to process: "))
    output = str(input("Enter path to result video: "))

    capture = cv2.VideoCapture(filename)
    fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
    video_recorder = cv2.VideoWriter(output, fourcc, 20.0, (int(capture.get(3)), int(capture.get(4))))
    current_len_of_circles = 0

    while capture.isOpened():
        ret, frame = capture.read()
        if frame is None:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=40, minRadius=50, maxRadius=100)

        count = 0
        if circles is not None:
            len_of_circles = len(circles[0, :])
            if len_of_circles > current_len_of_circles:
                current_len_of_circles = len_of_circles
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                print(i)
                print(i)
                count += 1
                center = (i[0], i[1])
                # circle center
                cv2.circle(frame, center, 1, (0, 10, 10), 3)
                # circle outline
                radius = i[2]
                cv2.circle(frame, center, radius, (255, 0, 255), 3)
                font = cv2.FONT_HERSHEY_SIMPLEX

                font_scale = 2
                thickness = 3
                color = (255, 0, 0)

                cv2.putText(frame, str(count), center, font, font_scale, color, thickness, cv2.LINE_AA)

        video_recorder.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def getTextInfo(fileName, count_or_circles):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    save_video_result()
