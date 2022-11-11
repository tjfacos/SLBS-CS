close all;
clear all;
clc;

C = imread("PlaneGrey.jpg")
figure(1)
imshow(C)

C(:,:) = 255 - C(:,:)
figure(2)
imshow(C)
imwrite(C, "PlaneNegative.jpg")