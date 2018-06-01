# Fisheye camera calibration

Camera calibration example for:
TUM Visual-Inertial Dataset


https://github.com/ethz-asl/kalibr/wiki/supported-models

pinhole camera model (pinhole) 
(intrinsics vector: [fu fv pu pv])
```
K = 
fu 0  pu
0  fv pv
0  0  1
```

equidistant (equi)
(distortion_coeffs: [k1 k2 k3 k4])

## Before calibration
![](./1.png)

## After calibration
![](./out.png)
