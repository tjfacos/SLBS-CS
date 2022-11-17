close all;
clear all;


fs = 2e4;
freq = 1000;
t = 0:1/2e4:1-(1/2e4);
tone = 1/2*cos(2*pi*freq*t);
audiowrite("Tone1.wav", tone, fs);

