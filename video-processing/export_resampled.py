import numpy as np
import cv2

import os
import sys

import pickle

vwindow = (310, 410)
hwindow = 8

if __name__ == '__main__':
    ifn = sys.argv[1]
    ofn = sys.argv[2]
    if os.path.exists(ifn):
        print("Input: " + os.path.basename(ifn))
        print("Output: " + os.path.basename(ofn))
    else:
        print('Invalid path. Try again...')
        sys.exit()

    cap = cv2.VideoCapture(ifn)
    frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    
    output = np.zeros((frames, 150, 3))
    cap.isOpened()

    for i in range(frames):
        ret, frame = cap.read()

        spl = np.split(frame[vwindow[0]:vwindow[1]], range(hwindow, 151 * hwindow, hwindow), axis=1)
        rs_frame = np.array(spl[:-1]).mean(axis=1).mean(axis=1)

        output[i] = rs_frame
        print(i)

        # cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(output.shape)

    with open(ofn, 'wb') as pklfile:
        pickle.dump(output, pklfile)

    cap.release()
    cv2.destroyAllWindows()
