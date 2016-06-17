import hashlib

newyork = ['thebronx','brooklyn','manhattan','queens','richmond','statenisland']
md5="6ac66ed89ef9654cf25eb88c21f4ecd0".encode("utf-8");
for num1 in range(0,1000):
	for num2 in range(10000,15000):
		for index in newyork:
			strs="ctf{"+str(num1).encode("utf-8")+"_"+index+"_"+str(num2).encode("utf-8")+"}"
			m2 = hashlib.md5(strs.encode("utf-8"))   
			m2.update(strs)   
			MD5=m2.hexdigest()
			if MD5==md5:
				print strs