clear all;
close all;
clc;

M = imread("MilesP.jpg")
figure(1);
imshow(M);

B = M;
B(:,:,1) = 0.5*B(:,:,1)
B(:,:,2) = 0.5*B(:,:,2)
figure(2)
imshow(B)
imwrite(B, "MilesB.jpg")