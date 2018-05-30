import cv2
import yaml
from matplotlib.pyplot import imshow
import numpy as np



def undistort():
    skip_lines = 0
    with open('./pinhole-equi-512/camchain-imucam-imucalib.yaml') as infile:
        for i in range(skip_lines):
            _ = infile.readline()
        data = yaml.load(infile)
        
        
    # You should replace these 3 lines with the output in calibration step
    DIM=(512, 512)
    #K=np.array(YYY)
    #D=np.array(ZZZ)


    [fu, fv, pu, pv] = data['cam0']['intrinsics']
    #https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0
    K = np.asarray([[fu, 0, pu], [0, fv, pv], [0, 0, 1]]) # K(3,3)
    D = np.asarray(data['cam0']['distortion_coeffs'])#D(4,1)
    
    
    img = cv2.imread("1.png")
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    
    cv2.imwrite("out.png", undistorted_img)
    #imshow(undistorted_img, cmap='gray')
    #cv2.imshow("undistorted", undistorted_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
if __name__ == '__main__':
    undistort()    
