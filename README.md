# Camera distortion calibration

Image undistortion example with OpenCV Python for **TUM Visual-Inertial Dataset**

## Camera geometric model
(Reference: https://github.com/ethz-asl/kalibr/wiki/supported-models)
Two key parameters is been used for geometric calibration:
1. Intrinsic model
2. distortion model

## Camera model
---
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
---

## Distortion model

equidistant (equi)
(distortion_coeffs: [k1 k2 k3 k4])

## Before calibration
![](./1.png)

## After calibration
![](./out.png)
