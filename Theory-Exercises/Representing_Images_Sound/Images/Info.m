close all;
clear all;
clc;

I = imread("GLaDOS.jpg");
figure(1);
imshow(I);


G = I;

G(:,:,1) = ((0.299 * G(:,:,1)) + (0.587 * G(:,:,2)) + (0.114 * G(:,:,3))) / 3;
G(:,:,2) = ((0.299 * G(:,:,1)) + (0.587 * G(:,:,2)) + (0.114 * G(:,:,3))) / 3;
G(:,:,3) = ((0.299 * G(:,:,1)) + (0.587 * G(:,:,2)) + (0.114 * G(:,:,3))) / 3;

figure(2);
imshow(G);
