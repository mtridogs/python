%[f1,f2,f3,f4,class] = textread('trainData.txt' , '%f%f%f%f%f',150);
%
%clc
%clear
load C:\Users\dell\Desktop\毕业论文\matlab\KDD\test;
%load C:\Users\dell\Desktop\毕业论文\matlab\KDD\att0;
% load C:\Users\dell\Desktop\毕业论文\matlab\KDD\att1;
% load C:\Users\dell\Desktop\毕业论文\matlab\KDD\att2;
% load C:\Users\dell\Desktop\毕业论文\matlab\KDD\att3;
% load C:\Users\dell\Desktop\毕业论文\matlab\KDD\att4;
bpinput_att0=test(1:40000,1:41);
output_att0=test(1:40000,42);

net=BP_train(bpinput_att0,output_att0);
