function BPoutput = BPreport(net,input_test,testoutput)
input_test = input_test';
BPoutput=sim(net,input_test);
rigerr =zeros(1,length(BPoutput));
for num=1:length(BPoutput)
    if (testoutput(num,1)==0&&BPoutput(1,num)<0.5)
        BPoutput(1,num)=0;
    elseif (testoutput(num,1)==1&&BPoutput(1,num)<1.5&&BPoutput(1,num)>=0.5)
        BPoutput(1,num)=1;
    elseif (testoutput(num,1)==2&&BPoutput(1,num)<2.5&&BPoutput(1,num)>1.5)
        BPoutput(1,num)=2;
    elseif (testoutput(num,1)==3&&BPoutput(1,num)<3.5&&BPoutput(1,num)>2.5)
        BPoutput(1,num)=3;
    elseif (testoutput(num,1)==4&&BPoutput(1,num)<4.5&&BPoutput(1,num)>3.5)
        BPoutput(1,num)=4;
    else 
        BPoutput(1,num)=-1;
    end
end


%
%
%
end

