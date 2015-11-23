import csv
import os
from random import uniform
import time
import math

__author__ = 'matteo'

def __initData(path,nome,dataset,test,nTest):

    with open(path+'LOG','a+r') as log:
        counter = 0
        wr1 = csv.writer(log, dialect="excel-tab")
        for line in csv.reader(log, dialect="excel-tab"):
            if nome in line[0]:
                counter = int(line[1])

        if counter == 0:
            number = 1
        elif counter == nTest:
            return path+nome+'_'+str(counter)+'/'
        else:
            number = int(counter)+1

        index = '_' +str(number)
        if not os.path.exists(path+nome+index):
            os.makedirs(path+nome+index)
            wr1.writerow([nome,number,'dataset = '+dataset+ ' - training_set='+ str(100-test)+'% test_set='+str(test)+'% ',time.strftime('%d-%m-%Y %H:%M:%S')])

        return path+nome+index+'/'

def __addNote(path,note):
    with open(path+'LOG','a') as log:
        wr1 = csv.writer(log, dialect="excel-tab")
        wr1.writerow(['  -',note,'  '+ time.strftime('%d-%m-%Y %H:%M:%S')])



def __timeStampOrd__(test,path,PATH):
    list = []
    with open(path+'u.data') as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            list.append(line)

    tsv.close()
    list.sort(key=lambda list: list[3])

    print (len(list)*(100-test)/100)
    with open(PATH+'dataTraining','w') as file1:
        wr = csv.writer(file1, dialect='excel')
        for i in range(0,(len(list)*(100-test)/100)):
            wr.writerow(list[i])
        file1.close()

    with open(PATH+'dataTest','w') as file2:
        wr = csv.writer(file2, dialect='excel')
        for i in range ((len(list)*(100-test)/100),len(list)):
            wr.writerow(list[i])

        file2.close()



def __randomSampleOrd__(test,path,PATH):
    with open(PATH+'dataTraining','w') as file1:
        with open(PATH+'dataTest','w') as file2:
            wr1 = csv.writer(file1, dialect='excel')
            wr2 = csv.writer(file2, dialect='excel')
            with open(path+'u.data') as tsv:
                for line in csv.reader(tsv, dialect="excel-tab"):
                    if uniform(0,10)>float(test/10):
                        wr1.writerow(line)
                    else:
                        wr2.writerow(line)


def __getData__(test,path,PATH,X,Y,SaveToDisk=True,timeStampOrd=False):
    Matrix = [[0 for x in range(X)] for y in range(Y)]
    if timeStampOrd:
        if SaveToDisk:
            __timeStampOrd__(test,path,PATH)

        with open(PATH+'dataTraining', 'r') as read1:
            for line in csv.reader(read1, dialect="excel"):
                Matrix[int(line[0])-1][int(line[1])-1] = int(line[2])
            read1.close()
    else:
        if SaveToDisk:
            __randomSampleOrd__(test,path,PATH)

        with open(PATH+'dataTraining', 'r') as read2:
            for line in csv.reader(read2, dialect="excel"):
                Matrix[int(line[0])-1][int(line[1])-1] = int(line[2])
            read2.close()
    return Matrix


def __AverageLUxU__(Matrix):
    AverageList = []
    for i in range(0,len(Matrix)):
        counter = 0
        somma = 0
        for j in range(0,len(Matrix[i])):
            if Matrix[i][j] != 0:
                somma += Matrix[i][j]
                counter += 1
        if counter != 0:
            AverageList.append(somma/float(counter))
        else:
            print 'WARNING AverageList = 0 for user = ' +str(i)
            AverageList.append(0)

    return AverageList

def __AverageLIxI__(Matrix):
    AverageList = []
    for j in range(0,len(Matrix[0])):
        counter = 0
        somma = 0
        for i in range(0,len(Matrix)):
            if Matrix[i][j] != 0:
                somma += Matrix[i][j]
                counter += 1
        if counter != 0:
            AverageList.append(somma/float(counter))
        else:
            print 'WARNING AverageList = 0 for item = ' +str(i)
            AverageList.append(0)

    return AverageList



def __similIxI__(Matrix,PATH,X,Written=False):
    #The Pearson correlation similarity Item-Item
    AverageList = __AverageLIxI__(Matrix)
    SimilMatrix = [[0 for x in range(X)] for y in range(X)]
    if Written:
        with open(PATH+'SimilMatrixIxI','r') as SM:
            counterLine = 0
            for line in csv.reader(SM, dialect="excel"):
                for i in range(0,len(SimilMatrix)):
                    SimilMatrix[counterLine][i] = line[i]
                counterLine +=1
            SM.close()
    else:
        for i in range(0,len(SimilMatrix)):
            for j in range(0,len(SimilMatrix)):
                if i>j:
                    numeratore = 0
                    denominatore = 0
                    for k in range(0,len(Matrix)):
                        if (Matrix[k][i] != 0 ) and (Matrix[k][j] != 0):
                            membro_i = Matrix[k][i]-AverageList[i]
                            membro_j = Matrix[k][j]-AverageList[j]
                            numeratore += membro_i * membro_j
                            denominatore += (membro_i**2) * (membro_j**2)
                    if denominatore != 0:
                        SimilMatrix[i][j] = numeratore/math.sqrt(denominatore)
                        SimilMatrix[j][i] = numeratore/math.sqrt(denominatore)

        with open(PATH+'SimilMatrixIxI','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for i in SimilMatrix:
                wr.writerow(i)

            SM.close()

    return SimilMatrix








def __similUxU__(Matrix,PATH,Y,Written=False):
    #The Pearson correlation similarity User-User
    AverageList = __AverageLUxU__(Matrix)
    SimilMatrix = [[0 for x in range(Y)] for y in range(Y)]
    if Written:
        with open(PATH+'SimilMatrixUxU','r') as SM:
            counterLine = 0
            for line in csv.reader(SM, dialect="excel"):
                for i in range(0,len(SimilMatrix)):
                    SimilMatrix[counterLine][i] = line[i]
                counterLine +=1
            SM.close()
    else:
        for i in range(0,len(SimilMatrix)):
            for j in range(0,len(SimilMatrix)):
                if i>j:
                    numeratore = 0
                    denominatore = 0
                    for k in range(0,len(Matrix[0])):
                        if (Matrix[i][k] != 0 ) and (Matrix[j][k] != 0):
                            membro_i = Matrix[i][k]-AverageList[i]
                            membro_j = Matrix[j][k]-AverageList[j]
                            numeratore += membro_i * membro_j
                            denominatore += (membro_i**2) * (membro_j**2)
                    if denominatore != 0:
                        SimilMatrix[i][j] = numeratore/math.sqrt(denominatore)
                        SimilMatrix[j][i] = numeratore/math.sqrt(denominatore)

        with open(PATH+'SimilMatrixUxU','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for i in SimilMatrix:
                wr.writerow(i)

            SM.close()

    return SimilMatrix


