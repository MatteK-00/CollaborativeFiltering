__author__ = 'matteo'


#u.data     -> user id | item id | rating | timestamp
#u.info     -> The number of users, items, and ratings in the u data set.
#u.item     -> movie id | movie title | release date | video release date |
#              IMDb URL | unknown | Action | Adventure | Animation |
#              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
#              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
#              Thriller | War | Western |
#u.genre    -> A list of the genres
#u.user     -> user id | age | gender | occupation | zip code
#u.occupation -> A list of the occupations.

# numero utenti: 943  numero film: 1682

import csv
import math
import os
import re
import time
from random import randrange, uniform
import heapq
from datetime import datetime
import calendar


def __AverageL__(Matrix):
    AverageList = []
    for i in range(0,len(Matrix)):
        counter = 0
        somma = 0
        for j in range(0,len(Matrix[i])):
            if Matrix[i][j] != 0:
                somma += j
                counter += 1
        if counter != 0:
            AverageList.append(somma/float(counter))
        else:
            print 'WARNING AverageList = 0 for user = ' +str(i)
            AverageList.append(0)

    return AverageList


def __simil__(Matrix,PATH,Written=False):
    #The Pearson correlation similarity
    AverageList = __AverageL__(Matrix)
    SimilMatrix = [[0 for x in range(943)] for y in range(943)]
    if Written:
        with open(PATH+'SimilMatrix','r') as SM:
            counterLine = 0
            for line in csv.reader(SM, dialect="excel"):
                for i in range(0,len(SimilMatrix)):
                    SimilMatrix[counterLine][i] = line[i]
                counterLine +=1
            SM.close()
    else:
        for i in range(0,len(SimilMatrix)):
            for j in range(0,len(SimilMatrix)):
                #if i<j:
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

        with open(PATH+'SimilMatrix','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for i in SimilMatrix:
                wr.writerow(i)

            SM.close()

    return SimilMatrix





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


def __getData__(test,path,PATH,timeStampOrd=False,SaveToDisk=True):
    Matrix = [[0 for x in range(1682)] for y in range(943)]
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


def __initData(path,nome,dataset,test,note,nTest):
    with open(path+'LOG','a+r') as log:
        lines = log.readlines()
        counter = []
        n = []
        if len(lines)>=1:
            last = lines[-1]
            counter = re.findall('\d',last)
            n = (re.findall(nome,last))

        if n == []:
            number = '_1'
        elif int(counter[0]) == nTest:
            return path+nome+'_'+str(nTest)+'/'
        else:
            number = '_'+ str(int(counter[0])+1)

        if not os.path.exists(path+nome+number):
            os.makedirs(path+nome+number)
            log.write(nome+number + ' [dataset = '+dataset+ ' - training_set='+ str(100-test)+'% test_set='+str(test)+'% '+ ' - Note: '+note+ ']: ' +time.strftime('%d-%m-%Y %H:%M:%S') +'\n')

        return path+nome+number+'/'

def __UserRatingPrediction__(k,PATH,Matrix,SimilMatrix):
    res = []
    with open(PATH+'dataTest','r') as testLine:
        with open (PATH+'UserRatingPrediction','w') as URP:
            wr1 = csv.writer(URP, dialect='excel')
            for line in csv.reader(testLine, dialect="excel"):
                usr_u = int(line[0])-1
                item_i = int(line[1])-1
                usr_v = []
                for i in range(0,len(SimilMatrix)):
                    if Matrix[i][item_i] != 0:
                        usr_v.append([SimilMatrix[usr_u][i],Matrix[i][item_i]])
                if usr_v == []:
                    print 'WARNING no entry for '+ str(usr_u) +' ' +str(item_i)
                else:
                    k2 = min(k,len(usr_v))
                    adj_u=heapq.nlargest(k2,usr_v)
                    sum = 0.0
                    for j in range(0,k2):
                        sum += adj_u[j][1]
                    r_ui = 1/float(k)*sum
                    wr1.writerow([k2,usr_u+1,item_i+1,r_ui,line[2]])
                    res.append([k2,usr_u+1,item_i+1,r_ui,line[2]])

    URP.close()
    testLine.close()


    return res


def __RMSE_MAE__(PATH):
    #Measuring Ratings Prediction Accuracy by RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error)
    with open(PATH+'UserRatingPrediction', 'r+a') as URP:
        counterLine=0;
        RSME = 0.0
        MAE = 0.0
        for line in csv.reader(URP, dialect="excel"):
            #print line[3] + ' ' + line[4] + ' ' + str(counterLine)
            temp = float(line[3]) - int(line[4])
            MAE += abs(temp)
            RSME += temp**2
            counterLine += 1

        RSME = math.sqrt(1.0/counterLine*RSME)
        MAE = math.sqrt(1.0/counterLine*MAE)
        sol = 'RSME = ' + str(RSME) + ' NRSME = '+ str(RSME/(5-1)) + ' MAE = ' + str(MAE) + ' NMAE = ' + str(MAE/(5-1))
        print sol
        #URP.write(sol)



def main(nome,test,nTest=None,note='',dataset='MovieLens',path='/home/matteo/Desktop/DataMining/ml-100k/'):


    #Matrix = [[0 for x in range(1682)] for y in range(943)]
    #AverageList = []
    #SimilMatrix = [[0 for x in range(943)] for y in range(943)]
    PATH = __initData(path,nome,dataset,test,note,nTest)

    print PATH




    Matrix = __getData__(test, path, PATH, False,False)


    SimilMatrix = __simil__(Matrix,PATH,True)


    res = __UserRatingPrediction__(6,PATH,Matrix,SimilMatrix)

    __RMSE_MAE__(PATH)

    #print res




    # with open('/home/matteo/Desktop/DataMining/ml-100k/u.dataTIMESTAMP','w') as TST:
    #     with open('/home/matteo/Desktop/DataMining/ml-100k/u.data') as tsv:
    #         for line in csv.reader(tsv, dialect="excel-tab"):
    #             Matrix[int(line[0])-1][int(line[1])-1] = int(line[2])
    #             TST.write("%s\n" % datetime.datetime.fromtimestamp(float(line[3])).strftime('%Y-%m-%d %H:%M:%S'))
    # tsv.close()
    # TST.close()
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # with open('/home/matteo/Desktop/DataMining/ml-100k/u.SimilMatrix','w') as sMat:
    #     for item in SimilMatrix:
    #          sMat.write("%s\n" % item)
    # sMat.close()
    #
    # with open('/home/matteo/Desktop/DataMining/ml-100k/u.matrix','w') as mat:
    #      for item in Matrix:
    #          mat.write("%s\n" % item)
    # mat.close()


if __name__ == "__main__":
    #main('test',10,4,'Test completo creazione dati (randomSample) tabelle e calcolo errore predizione')
    main('Test',10,7,'Test completo creazione dati (randomSample) tabelle e calcolo errore predizione')


# class User:
#
#     def __init__(self,user_id,age,gender,occupation,zip_code):
#         self.user_id = user_id
#         self.dx = age
#         self.sx = gender
#         self.goal = occupation
#         self.mossa = zip_code
#         self.n_recensioni = 1
#
#     def __addCounter(self,n_recensioni):
#         n_recensioni+=1
