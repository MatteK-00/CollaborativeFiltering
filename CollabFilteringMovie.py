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
from sets import Set
from datetime import datetime
import calendar




def __ReferenceRankig__(Matrix):
    #Reference Ranking pag 277
    RefRank = []
    for i in range (0,len(Matrix)):
        user_pref = []
        for j in range (0,len(Matrix[0])):
            if Matrix[i][j] != 0:
                user_pref.append((Matrix[i][j],j))
        user_pref.sort(None,None,True)
        RefRank.append(user_pref)

    return RefRank


def __RecommenderSystem__(MatrixSimil):
    print ('?')



def __UsagePredictionCFPROVA__ (K,PATH,Matrix,SimilMatrix):
    # PROVA RECOMENDER SYSTEM
    res = []
    usersToTest = []
    itemsForUser = []

    #Creo la lista degli utenti a cui proporre item e la lista degli item effettivamente scelti dagli utenti
    with open(PATH+'dataTest','r') as testLine:
        for line in csv.reader(testLine, dialect="excel"):
            if int(line[0])-1 not in usersToTest:
                usersToTest.append(int(line[0])-1)
                itemsForUser.append((int(line[0])-1,[int(line[1])-1]))
            else:
                for i in itemsForUser:
                    if i[0] == int(line[0])-1:
                        i[1].append(int(line[1])-1)

    testLine.close()

    #Per ogni utente nella lista cerco gli utenti a lui più simili e estraggo gli oggetti a loro più graditi,
    #conto gli oggetti ripetuti più spesso e consiglio ad ogni utente k2 di questi
    with open (PATH+'UsagePrediction','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        for usr_u in usersToTest:
            users_v = []
            for i in range(0,len(SimilMatrix)):
                if SimilMatrix[usr_u][i] != 0:
                    users_v.append([SimilMatrix[usr_u][i],i])
            k2 = min(K,len(users_v))
            users_simil = heapq.nlargest(k2,users_v)
            filmToRank = []
            for u in range(0,len(users_simil)):
                for j in range(0,len(Matrix[0])):
                    if (Matrix[users_simil[u][1]][j] !=0):
                        #filmToRank.append((i,Matrix[u][j]))
                        filmToRank.append((j))
            HASH = Set(filmToRank)
            temprank = []
            for i in HASH:
                temprank.append((filmToRank.count(i),i))
            temprank2 = heapq.nlargest(k2,temprank)

            rank = []
            for i in temprank2:
                rank.append(i[1])

            TP = FN = FP = TN = 0
            temp = []
            for k in itemsForUser:
                if k[0] == usr_u:
                    temp = k[1]
                    for i in k[1]:
                        if i in rank:
                            TP += 1
                        else:
                            FN += 1
                    for j in rank:
                        if j in k[1]:
                            FP += 1
                        else:
                            TN += 1


            resP = [TP,FN,FP,TN]
            res.append(resP)
            wr1.writerow([usr_u,'TP = '+str(TP) +' FN = '+str(FN)+' FP = '+str(FP)+' TN = '+str(TN),temp, rank]) #, Precision,Recall.FalsePositiveRate)

        tp = fn = fp = tn = 0
        for i in res:
            tp += i[0]
            fn += i[1]
            fp += i[2]
            tn += i[3]

        print 'TP =' +str(tp)
        print 'FN ='+ str(fn)
        print 'FP ='+ str(fp)
        print 'TN ='+ str(tn)

        Precision = (float(tp))/(tp+fp)
        Recall = (float(tp))/(tp+fn)
        FalsePositiveRate = (float(fp))/(fp+tn)

        wr1.writerow(['Precision = ' +str(Precision) +' Recall = ' + str(Recall) +' FalsePositiveRate = ' + str(FalsePositiveRate)])


    return 'Precision = ' +str(Precision) +' Recall = ' + str(Recall) +' FalsePositiveRate = ' + str(FalsePositiveRate)








# def main(nome,test,nTest=None,dataset='MovieLens',path='/home/matteo/Desktop/DataMining/ml-100k/',X=0,Y=0):
#
#     if dataset == 'MovieLens':
#         path='/home/matteo/Desktop/DataMining/ml-100k/'
#         X=1682
#         Y=943
#     elif dataset == 'yelp':
#         path='/home/matteo/Desktop/DataMining/yelp_dataset_academic/'
#         X=13490
#         Y=130873
#
#     #Matrix = [[0 for x in range(1682)] for y in range(943)]
#     #AverageList = []
#     #SimilMatrix = [[0 for x in range(943)] for y in range(943)]
#     PATH = __initData(path,nome,dataset,test,nTest)
#
#     print PATH
#     __addNote(path,'prova note')
#
#
#
#     Matrix = __getData__(test, path, PATH,X,Y, False)
#     #print __ReferenceRankig__(Matrix)
#
#     SimilMatrix = __simil__(Matrix,PATH,Y,False)
#     #print __UsagePrediction__(15,PATH,Matrix,SimilMatrix)
#
#     #res = __UserRatingPrediction__(6,PATH,Matrix,SimilMatrix)
#
#     #TODO: aggiungere nei log le misurazioni!
#     #__RMSE_MAE__(PATH)
#
#     #print res
#
#
#
#
#     # with open('/home/matteo/Desktop/DataMining/ml-100k/u.dataTIMESTAMP','w') as TST:
#     #     with open('/home/matteo/Desktop/DataMining/ml-100k/u.data') as tsv:
#     #         for line in csv.reader(tsv, dialect="excel-tab"):
#     #             Matrix[int(line[0])-1][int(line[1])-1] = int(line[2])
#     #             TST.write("%s\n" % datetime.datetime.fromtimestamp(float(line[3])).strftime('%Y-%m-%d %H:%M:%S'))
#     # tsv.close()
#     # TST.close()
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     # with open('/home/matteo/Desktop/DataMining/ml-100k/u.SimilMatrix','w') as sMat:
#     #     for item in SimilMatrix:
#     #          sMat.write("%s\n" % item)
#     # sMat.close()
#     #
#     # with open('/home/matteo/Desktop/DataMining/ml-100k/u.matrix','w') as mat:
#     #      for item in Matrix:
#     #          mat.write("%s\n" % item)
#     # mat.close()
#
#
# if __name__ == "__main__":
#     main('PROVA',10,1)
#     #main('Test_YELP',10,8,'Test completo creazione dati (randomSample) tabelle e calcolo errore predizione','yelp')


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
