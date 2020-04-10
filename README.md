# Doolittle-Algorithm-LU-decomposition
Doolittle Algorithm LU decomposition for solving linear equations


Solve the following system of simultaneous linear equations using LU decomposition method. 
 
𝟓𝒙𝟏 + 𝟔𝒙𝟐 + 𝟐.𝟑𝒙𝟑 + 𝟔𝒙𝟒 = 𝟒  
𝟗𝒙𝟏 + 𝟐𝒙𝟐 + 𝟑.𝟓𝒙𝟑 + 𝟕𝒙𝟒 = 𝟓    
𝟑.𝟓𝒙𝟏 + 𝟔𝒙𝟐 + 𝟐𝒙𝟑 + 𝟑𝒙𝟒 = 𝟔.𝟕 
𝟏.𝟓𝒙𝟏 + 𝟐𝒙𝟐 + 𝟏.𝟓𝒙𝟑 + 𝟔𝒙𝟒 = 𝟕.𝟖 
 
This program has been written in python


outputs :

Matrix L: 
[[ 1.          0.          0.          0.        ]
 [ 1.8         1.          0.          0.        ]
 [ 0.7        -0.20454545  1.          0.        ]
 [ 0.3        -0.02272727  3.07017544  1.        ]] 
 
Matrix U: 
[[ 5.          6.          2.3         6.        ]
 [ 0.         -8.8        -0.64       -3.8       ]
 [ 0.          0.          0.25909091 -1.97727273]
 [ 0.          0.          0.         10.18421053]]

Matrix Y: 
[ 4.         -2.2         3.45       -4.04210526]

Matrix X: 
[-3.06356589 -0.32674419 10.28682171 -0.39689922]


Process finished with exit code 0



Thanx to https://github.com/msaw97/metody4-gauss-elimination for sharing his code ,to help me understand


