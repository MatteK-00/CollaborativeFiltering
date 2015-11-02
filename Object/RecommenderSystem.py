import csv
import heapq
from sets import Set

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
    with open (PATH+'UsagePrediction','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        RES = []

        for UT in range(0,len(UserTest)):
            temp = []
            temp2 = []
            res = []
            Simil_id = __getK_Simil__(SimilMatrix,UserTest[UT].usr_id,K)
            for i in Simil_id:
                temp += heapq.nlargest(K,UserList[i[1]].usr_rw)
            for j in temp:
                temp2.append(j[1])
            for l in temp2:
                res.append((temp2.count(l),l))
            res = Set(res)
            res = heapq.nlargest(K,res)

            racommendedList = []
            userTestList = UserTest[UT].extractItem()
            TP = FN = TN = FP = 0
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
                else:
                    TN += 1

            resP = [TP,FN,FP,TN]
            RES.append(resP)
            wr1.writerow([UserTest[UT].usr_id,'TP = '+str(TP) +' FN = '+str(FN)+' FP = '+str(FP)+' TN = '+str(TN),userTestList, racommendedList]) #, Precision,Recall.FalsePositiveRate)

        tp = fn = fp = tn = 0
        for i in RES:
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

        URP.close()


    return 'Precision = ' +str(Precision) +' Recall = ' + str(Recall) +' FalsePositiveRate = ' + str(FalsePositiveRate)


def __recSystemObjIxI__(K,ItemList,ItemTest,SimilMatrix,Y,PATH):
    with open (PATH+'UsagePrediction','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        RES = []

        for UT in range(0,len(ItemTest)):
            temp  = []
            temp2 = []
            res = []
            Simil_id = __getK_Simil__(SimilMatrix,ItemTest[UT].usr_id,K)
            for i in Simil_id:
                temp += heapq.nlargest(K,ItemList[i[1]].usr_rw)
            for j in temp:
                temp2.append(j[1])
            for l in temp2:
                res.append((temp2.count(l),l))
            res = Set(res)
            res = heapq.nlargest(K,res)

            racommendedList = []
            ItemTestList = ItemTest[UT].extractItem()
            TP = FN = TN = FP = 0
            for i in res:
                racommendedList.append(i[1])

            for rl in racommendedList:
                if rl in ItemTestList:
                    TP +=1
                else:
                    FP +=1
            for ur in ItemTestList:
                if ur not in racommendedList:
                    FN += 1
                else:
                    TN += 1

            resP = [TP,FN,FP,TN]
            RES.append(resP)
            wr1.writerow([ItemTestList[UT].usr_id,'TP = '+str(TP) +' FN = '+str(FN)+' FP = '+str(FP)+' TN = '+str(TN),ItemTestList, racommendedList]) #, Precision,Recall.FalsePositiveRate)

        tp = fn = fp = tn = 0
        for i in RES:
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

        URP.close()


    return 'Precision = ' +str(Precision) +' Recall = ' + str(Recall) +' FalsePositiveRate = ' + str(FalsePositiveRate)
