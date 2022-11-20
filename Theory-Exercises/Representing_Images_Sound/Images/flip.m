close all;
clear all;
clc;

pkg load image;

C = imread("GLaDOS.jpg");
imrotate(C, 180);

figure(1);
imshow(C);
