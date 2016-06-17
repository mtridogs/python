test_train = test(10000:100000,1:41);
test_train_out = test(10000:100000,42);
BP_KDD_att0 = BPreport(net,test_train,test_train_out);
