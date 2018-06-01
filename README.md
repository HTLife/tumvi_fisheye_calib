# Image distortion calibration

Image undistortion example with OpenCV Python for **TUM Visual-Inertial Dataset**

## Camera geometric model
(Reference: https://github.com/ethz-asl/kalibr/wiki/supported-models)

Two key parameters is been used for geometric calibration:
1. Intrinsic model
2. distortion model

## Camera model

### Omnidirectional
omnidirectional camera model (omni) 
(intrinsics vector: [xi fu fv pu pv])

The intrinsics vector contains all parameters for the model:
  * fu, fv: focal-length
  * pu, pv: principal point
  * xi: mirror parameter (only omni)
```
K = 
fu*fu cot(xi) pu
0     fv      pv
0     0       1
```
### Pinhole
pinhole camera model (pinhole) 
(intrinsics vector: [fu fv pu pv])
```
K = 
fu    0       pu
0     fv      pv
0     0       1
```


## Distortion model

equidistant (equi)
(distortion_coeffs: [k1 k2 k3 k4])

## Before calibration (pinhole model)
![](./1.png)

## After calibration (pinhole model)
![](./out.png)



# Matlab example
https://github.com/ethz-asl/kalibr/files/272054/Undistort.m.txt
```matlab
imageD = imread('1.png');
% pinhole-equi-512
intri = [190.97847715128717, 190.9733070521226, 254.93170605935475, 256.8974428996504];
D = [0.0034823894022493434, 0.0007150348452162257, -0.0020532361418706202, 0.00020293673591811182];
fu = intri(1);
fv = intri(2);
pu = intri(3);
pv = intri(4);

K = [fu 0 pu
    0 fv pv
    0 0 1];
unImg = Undistort(imageD, D, K, 'equi');
imshow(unImg);
```
