#-*-coding:utf-8-*-
import pickle
import numpy
from PIL import Image

def unpickle(file):
    fo = open(file,'rb')
    dict = pickle.load(fo,encoding='latin-1')
    #dict = pickle.load(fo) #python2.7
    fo.close()
    return dict

x_train = None
y_train = []

if __name__ == '__main__':
    data = unpickle('cifar-10-batches-py/data_batch_1')
    d = data['data'][9]
    #ref: http://aidiary.hatenablog.com/entry/20151014/1444827123
    #チャンネル,縦,横に分割して次元を入れ替えてる
    pilImg = Image.fromarray(numpy.uint8(d.reshape(3,32,32).transpose(1,2,0)),'RGB')
    pilImg.show()
