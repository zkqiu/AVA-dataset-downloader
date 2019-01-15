import sys, urllib
import urllib.request

test_file = 'ava_file_names_test_v2.1.txt'

test = open(test_file,'r')
test_finish = open('test_finish.txt','a')
test_fail = open('test_fail.txt','a')
test_finish_read = open('test_finish.txt','r')
test_finish_filenames = test_finish_read.readlines()
test_finish_read.close()


filename = test.readline()
while filename:
    if filename in test_finish_filenames:
        filename = test.readline()
        continue
    filename = filename.strip('\n')
    url = 'https://s3.amazonaws.com/ava-dataset/test/'+filename
    save_path = 'video\\test\\'+filename
    try:
        urllib.request.urlretrieve(url, save_path)
    except urllib.error:
        test_fail.write(filename+'\n')
        filename = test.readline()
        continue
    print (filename)
    test_finish.write(filename+'\n')
    filename = test.readline()

test.close()
test_finish.colse()
test_fail.close()