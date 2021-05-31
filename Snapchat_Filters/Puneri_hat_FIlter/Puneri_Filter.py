import dlib
import cv2


def mask(frame, landmarks):
    imgPuneri = cv2.imread("Puneri.png", -1)
    orig_mask = imgPuneri[:, :, 3]
    orig_mask_inv = cv2.bitwise_not(orig_mask)
    imgPuneri = imgPuneri[:, :, 0:3]
    origPuneriHeight, origPuneriWidth = imgPuneri.shape[:2]

    PuneriWidth = abs(3 * (landmarks.part(37).x - landmarks.part(44).x))
    PuneriHeight = int(PuneriWidth * origPuneriHeight / origPuneriWidth)
    Puneri = cv2.resize(imgPuneri, (PuneriWidth, PuneriHeight), interpolation=cv2.INTER_AREA)
    mask = cv2.resize(orig_mask, (PuneriWidth, PuneriHeight), interpolation=cv2.INTER_AREA)
    mask_inv = cv2.resize(orig_mask_inv, (PuneriWidth, PuneriHeight), interpolation=cv2.INTER_AREA)
    y1 = int(landmarks.part(21).y - (PuneriHeight / 2)) - 50
    y2 = int(y1 + PuneriHeight)
    x1 = int(landmarks.part(27).x - (PuneriWidth / 2))
    x2 = int(x1 + PuneriWidth)
    roi = frame[y1:y2, x1:x2]
    roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    roi_fg = cv2.bitwise_and(Puneri, Puneri, mask=mask)
    frame[y1:y2, x1:x2] = cv2.add(roi_bg, roi_fg)

    return frame


def filter():
    """
    This function consists main logic of the program in which
    1. detect faces
    2. from 68 landmark points we detect eyes
    3. Applies Filter
    :return: None
    """

    # detector for detecting the face in the image
    detector = dlib.get_frontal_face_detector()
    # predictor of locating 68 landmark points from the face by using a pretrained model
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detecting faces in the frame
            faces = detector(frameGray)

            # if faces are present then locating the landmark points
            for face in faces:
                landmarks = predictor(frameGray, face)

                frame = mask(frame, landmarks)

            # for showing frames on the window named Detector
            cv2.imshow('Detector', frame)

            # for quiting the program press 'ESC'
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break

    # releasing all the frames we captured and destroying the windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filter()
