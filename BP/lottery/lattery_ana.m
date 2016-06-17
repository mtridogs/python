load D:\python\BP\lottery\lattery_data
bpinput_att0=lattery_data(:,1:1:6);
output_att0=lattery_data(:,7);

net=BP_train(bpinput_att0,output_att0);

 load D:\python\BP\lottery\parper_data;
 parper_data=parper_data';
 latt_p = sim(net,parper_data);