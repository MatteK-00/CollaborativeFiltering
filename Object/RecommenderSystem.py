import csv
import heapq
from sets import Set
import math

__author__ = 'matteo'

def __getK_Simil__(SimilMatrix, ID, k):
    listres = []
    for i in range (0,len(SimilMatrix)):
        if (SimilMatrix[ID][i] != 0):
            temp = SimilMatrix[ID][i]
        else:
            temp = SimilMatrix[i][ID]
        listres.append((temp, i))

    listres = heapq.nlargest(k,listres)
    return listres


def __recSystemObjUxU__(K,UserList,UserTest,SimilMatrix,Y,PATH):
    with open (PATH+'UsagePredictionUxU','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        RES = []

        for UT in range(0,len(UserTest)):
            temp = []
            temp2 = []
            res = []
            #Simil_id = __getK_Simil__(SimilMatrix,UserTest[UT].usr_id,K)
            Simil_id = []
            for i in SimilMatrix[UT]:
                Simil_id.append(i[1])
            for i in Simil_id:
                temp += heapq.nlargest(K,UserList[i].usr_rw)
            for j in temp:
                temp2.append(j[1])
            for l in temp2:
                res.append((temp2.count(l),l))
            res = Set(res)
            res = heapq.nlargest(K,res)

            racommendedList = []
            userTestList = UserTest[UT].extractItem()
            TP = FN = FP = 0
            for i in res:
                racommendedList.append(i[1])

            for rl in racommendedList:
                if rl in userTestList:
                    TP +=1
                else:
                    FP +=1
            for ur in userTestList:
                if ur not in racommendedList:
                    FN += 1


            resP = [TP,FN,FP]
            RES.append(resP)
            wr1.writerow([UserTest[UT].usr_id,'TP = '+str(TP) +'FP = '+str(FP),userTestList, racommendedList]) #, Precision,Recall.FalsePositiveRate)

        tp = fn = fp  = 0
        for i in RES:
            tp += i[0]
            fn += i[1]
            fp += i[2]


        print 'TP =' +str(tp)
        print 'FP ='+ str(fp)

        Precision = (float(tp))/(tp+fp)
        Recall = (float(tp))/(tp+fn)


        wr1.writerow(['Precision = ' +str(Precision) +' Recall = ' + str(Recall)])

        URP.close()


    return 'Precision = ' +str(Precision) +' Recall = ' + str(Recall) + ' TP =' +str(tp) + ' FP = '+ str(fp)



def __recSystemObjIxI__(K,User,UserTest,ItemList,SimilMatrix,Y,PATH):
    with open (PATH+'UsagePredictionIxI','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        RES = []


        for UT in range(0,len(UserTest)):
            Simil_id = []
            racommendedListTemp = []
            racommendedList = []
            racommendedPart = []
            racommendedListId = []
            bestUserItem = heapq.nlargest(K,User[UT].usr_rw)

            for item in bestUserItem:
                 Simil_id.append(item[1])

            for it in Simil_id:
                racommendedListTemp += SimilMatrix[it]

            for it_id in racommendedListTemp:
                racommendedPart.append(it_id[1])

            for l in racommendedPart:
                racommendedList.append((racommendedPart.count(l),l))

            racommendedList = Set(racommendedList)

            racommendedList = heapq.nlargest(K,racommendedList)

            for boh in racommendedList:
                racommendedListId.append(boh[1])



            UserTestList = UserTest[UT].extractItem()
            TP = FN  = FP = 0

            for rl in racommendedListId:
                if rl in UserTestList:
                    TP +=1
                else:
                    FP +=1
            for ur in UserTestList:
                if ur not in racommendedListId:
                    FN += 1
            resP = [TP,FN,FP]
            RES.append(resP)
            wr1.writerow([UT,' TP = '+str(TP) +' FP = '+str(FP),UserTestList, racommendedListId])

        tp = fn = fp  = 0
        for i in RES:
            tp += i[0]
            fn += i[1]
            fp += i[2]


        print 'TP =' +str(tp)
        print 'FP ='+ str(fp)

        Precision = (float(tp))/(tp+fp)
        Recall = (float(tp))/(tp+fn)

        wr1.writerow(['Precision = ' +str(Precision) +' Recall = ' + str(Recall)])

        URP.close()


    return 'Precision = ' +str(Precision) +' Recall = ' + str(Recall)  + ' TP = ' +str(tp) + ' FP = '+ str(fp)





def sigmoid(x):
  return 1 / (1 + math.exp(-x))

# def __NDPM__(User,UserTestList,RecommenderList):
#     res = []
#     for i in range(0,len(RecommenderList)):
#         if RecommenderList[i] in UserTestList: #C^+
#             sigmoid()*sigmoid((i+1)-(UserTestList.index(RecommenderList[i])-1))
#         else: #C^-
#
    #
    #
    #
    #
    # C_plus = res
    # return