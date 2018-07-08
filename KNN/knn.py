# encoding:utf-8

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels = ['A','A','B','B']
    return group,labels

def classify(input,dataSe t,label,k):

    dataSize = dataSet.shape[0]
    # 计算欧式距离
    diff = tile(input,(dataSize,1)) - dataSet
    sqdiff = diff ** 2
    # 得到训练样本和测试样本的欧氏距离
    squareDist = sum(sqdiff,axis = 1)
    dist = squareDist ** 0.5
    # 对距离进行排序
    sortedDistIndex = argsort(dist)

    classCount={}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        # 对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    # 选取出现的类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes   
