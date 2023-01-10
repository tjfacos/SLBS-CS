close all;
clear all;
clc;

C = imread("MilesMinor.jpg");

[x,y,z] = size(C);

for plane = 1 : z
  len = x
  for i = 1 : x
    for j = 1 : y:
      if i < x/2
        temp = C(i,j, plane);
        C(i,j,plane) = C(len, j, plane);
        C(len, j, plane) = temp;

      endif
    endfor
    len = len - 1
  endfor
endfor

