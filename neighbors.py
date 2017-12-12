import collections
import math
import operator
import csv
import random
#mengiput file dan membaginya ke dalam trainset dan testset dengan perbandingan split
def loadData(filename,train,test,split):
	with open(filename,'r')as data:
		reader =csv.reader(data)
		mydata=list(reader)
	n=split*len(mydata)
#sebelum mebagi data terlebih dahulu diacak dengan fungsi random
	random.shuffle(mydata)
	#print len(mydata)
	for x in range(len(mydata)-1):
		for y in range(len(mydata[x])-2):
			mydata[x][y]=float(mydata[x][y])
		if x < n:
			train.append(mydata[x])
			#print mydata[x]
		else:
			test.append(mydata[x])	
			#print mydata[x]
	
#cari jarak antara dua datum, length adalah banyak variable/feature yang ada pada datum
def euclidean(data1,data2, length):
	distance=0	
	for x in range(length):
		distance+=pow((data1[x]-data2[x]),2)
		return math.sqrt(distance)

#menghitung jarak ke semua node dan di sort
def neighbors(train, test,k):
#harus menghitung euclidean distance untuk semua nya dan disimpan dan diambil sebanyak k
	jarak=[]
	neighbors=[]
	n_attribute=len(test)-2	
#menghitung jarak test ke data trainset	
	for x in range(len(train)):
		#menghitung jarak test set ke train set ke x dengan euclidean distance
		jarakKex=euclidean(train[x],test,n_attribute)
		#menambahkan data train ke x dan jaraknya dengan datum test set
		jarak.append((train[x],jarakKex))
	#print (jarak)
	#mengurutkan data dalam variable jarak berdasarkan hasil perhitungan euclidean distance		
	jarak.sort(key=operator.itemgetter(1))
	#print (jarak)
	#mengambil data dalam variable sebanyak k(neighbors yang ditentukan)
	for x in range(k):
		neighbors.append((jarak[x][0],jarak[x][1]))
	#print (neighbors)
	return neighbors
#menentukan kelas
def kelas(neighbors):
	res=[]
	for x in range(len(neighbors)):
		res.append(neighbors[x][0][-1])
	#	print res
	n=collections.Counter(res)
	j=n.most_common()	
	return j[0][0]
#memprediksikan keakurasian
def akurasi(test,prediksi):
	acc=0
	for x in range(len(test)):
		if(test[x][-1]==prediksi[x]):
			acc+=1
		print ('prediksi' +repr(prediksi[x]) + ', actual ' +repr(test[x][-1]))
	acc =(float(acc)/len(test))*100.0
	#print 'acc '+repr(acc)
	return acc

prediksi=[]
trainset=[]
test=[]
#perbandingan trainset dan testset
n=0.7
filename='diabetes.csv'
#memanggil fungsi loadData dengan parameter file name, trainset, testset, n
loadData(filename,trainset,test,n) 
#print ('train '+repr(trainset))
#print ('test ' +repr(test))
for x in range(len(test)):
	tetangga = neighbors(trainset,test[x],3)
	print ("neighbor test datum"+str(x)+repr(tetangga))
	help=kelas(tetangga)
	print(help)
	prediksi.append(help)
#print (prediksi)
keakuratan = akurasi(test,prediksi)
print ('ke akuratan : ' +repr(keakuratan))
