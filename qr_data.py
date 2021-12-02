import cv2, json, qrcode
import numpy as np

def detect_qr_from_webcam(webcam_port):
    cap = cv2.VideoCapture(webcam_port)
# initialize the OpenCV QRCode detector
    while True:
        _, img = cap.read()
        # detect and decode
        # check if there is a QRCode in the image
        rect_img, data = get_qr_data(img)
        if data:
            cv2.imshow("img", img)
            resp = cv2.waitKey(0)
            if resp == 13:
                cap.release()
                cv2.destroyAllWindows()
                return data
            elif resp == ord("q"):
                break
        cv2.imshow("img", img)
        # Enter q to Quit
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return -1

def get_qr_data(img):
    raw_data, vertices_array = detect_qr(img)

    # check if there is a QRCode in the image
    if vertices_array is not None:
        vertices_int = vertices_array.astype(int)
        if raw_data:
            data = raw_data
            # data = json.loads(raw_data)
            # cv2.putText(
            #     img,
            #     text= data[:15] if len(data) > 15 else data,
            #     org=(ve,y+30),
            #     fontFace= cv2.FONT_HERSHEY_SIMPLEX,
            #     fontScale=1,
            #     color=(0,0,0),
            #     thickness=2,
            #     lineType=cv2.LINE_AA)
            cv2.rectangle(img, tuple(vertices_int[0][0]), tuple(vertices_int[0][2]),(255, 0, 0),5)
            return img, data
    return None, None

def detect_qr(img):
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)
    return data, vertices_array

def create_qr(json_data):
    return qrcode.make(json_data)

if __name__ == "__main__":
    print(detect_qr_from_webcam(0))
