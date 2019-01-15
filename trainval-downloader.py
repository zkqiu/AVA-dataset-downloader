import sys, urllib
import urllib.request

trainval_file = 'ava_file_names_trainval_v2.1.txt'

trainval = open(trainval_file, 'r')
trainval_finish = open('trainval_finish.txt','a')
trainval_fail = open('trainval_fail.txt','a')
trainval_finish_read = open('trainval_finish.txt','r')

trainval_finish_filenames = trainval_finish_read.readlines()
trainval_finish_read.close()

filename = trainval.readline()
while filename:
    if filename in trainval_finish_filenames:
        filename = trainval.readline()
        continue
    filename = filename.strip('\n')
    url = 'https://s3.amazonaws.com/ava-dataset/trainval/'+filename
    save_path = 'video\\trainval\\'+filename
    try:
        urllib.request.urlretrieve(url, save_path)
    except urllib.error:
        trainval_fail.write(filename+'\n')
        filename = trainval.readline()
        continue
    print (filename)
    trainval_finish.write(filename+'\n')
    filename = trainval.readline()

trainval.close()
trainval_finish.close()
trainval_fail.close()
