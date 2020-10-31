import numpy as np
import cv2
import imutils


def read_video_file():
    # filename = input("Enter video file name: ")
    filename = "resources/sample-5.mp4"
    return cv2.VideoCapture(filename)


def rescale_video_size(frame, percent=30):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def display_video_result():
    capture = read_video_file()
    while capture.isOpened():
        ret, frame = capture.read()

        frame = imutils.resize(frame, width=400)
        # smooth image
        bilateral_filtered_image = cv2.bilateralFilter(frame, 15, 150, 150)
        # detecting edges
        detected_edges = cv2.Canny(bilateral_filtered_image, 75, 200)
        # find contours
        contours, _ = cv2.findContours(detected_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contour_list = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            area = cv2.contourArea(contour)
            if (len(approx) > 8 & len(approx) < 23) & (area > 30):
                print(len(approx))
                contour_list.append(contour)

        cv2.drawContours(frame, contour_list, -1, (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


def detect_contours(frame):
    # ball_contours, hierarchy = cv2.findContours(frame, cv2.)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_video_result()
