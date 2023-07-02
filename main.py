#!/usr/bin/env python
import cv2
from colorama import Fore, Style

class QRCameraReader:
    def __init__(self):
        self.url =  0 # Default webcam is 0. If  IP webcam set the URL. Eg https://100.x.x.x/video
        
        self.window_name = 'QR Code Reader'
        self.delay = 1

    def start(self):
        print(Fore.BLUE + f"Starting QR Code Reader..." + Style.RESET_ALL)
        cap = cv2.VideoCapture(self.url)
        qr_detector = cv2.QRCodeDetector()
        print(Fore.CYAN +"Loading frames..." + Style.RESET_ALL)

        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                ret_qr, decoded_info, points, _ = qr_detector.detectAndDecodeMulti(frame)
                if ret_qr:
                    for s, p in zip(decoded_info, points):
                        if s:
                            print(Fore.GREEN + 'Detected Link: ' + Fore.BLUE + s + Style.RESET_ALL)
                            color = (0, 255, 0)
                        else:
                            color = (0, 0, 255)
                        p = p.astype(int)
                        frame = cv2.polylines(frame, [p], True, (0, 255, 0), 3)
                        frame = cv2.putText(frame, s, (p[0][0], p[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            cv2.imshow(self.window_name, frame)
            if cv2.waitKey(self.delay) & 0xFF == ord('q'):
                break
            
        cap.release()
        cv2.destroyAllWindows()
       

if __name__ == '__main__':
    qr = QRCameraReader()
    qr.start()
    print(Fore.YELLOW + "QR Code Reader is closed." + Style.RESET_ALL)