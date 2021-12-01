import cv2, json

def detect_qr_from_webcam(webcam_port):
    # cap = cv2.VideoCapture(webcam_port)
    #
    # detector = cv2.QRCodeDetector()
    #
    # qr_data = {}
    #
    # while (True):
    #     _, img = cap.read()
    #     data, vertices, _ = detector.detectAndDecode(img)
    #
    #     if vertices is not None:
    #         qr_data = json.loads(str(data))
    #         print(qr_data)
    #         print(verticles)
    #         break
    #
    #     cv2.imshow(img, "image")
    #     if cv2.waitKey(1) == ord(q):
    #         break
    # cap.release()
    # cv2.destroyAllWindows()
    cap = cv2.VideoCapture(0)
# initialize the OpenCV QRCode detector
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        # detect and decode
        data, vertices_array, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if vertices_array is not None:
            if data:
                break
      # display the result
        cv2.imshow("img", img)
        # Enter q to Quit
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    if data:
        return json.loads(data)
    else:
        return None


if __name__ == "__main__":
    detect_qr_from_webcam(0)
