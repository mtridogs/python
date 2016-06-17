function net = BP_train(inputmar,outputmar)%输入矩阵，输出是训练结果矩阵0,1
%输出矩阵
bpinput = inputmar';
output = outputmar';
%net = newff( minmax(input) ,[4 4] ,{'logsig' 'purelin'},'traingdx'); 
net = newff(bpinput,output,[7 5 3]); 
%设置训练参数
net.trainparam.show=50;
net.trainparam.epochs=500;
net.trainparam.goal=0.01;
net.trainParam.lr=0.01;

net = train(net,bpinput,output);
end