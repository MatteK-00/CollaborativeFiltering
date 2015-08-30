import csv
import heapq
import math
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





def __simil_UxU_ObjFull__(UserList,Y,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = [[0 for x in range(Y)] for y in range(Y)]
        with open(PATH+'SimilMatrixUxU','r') as SM:
            counterLine = 0
            for line in csv.reader(SM, dialect="excel"):
                for i in range(0,len(SimilMatrix)):
                    SimilMatrix[counterLine][i] = line[i]
                counterLine +=1
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixUxU','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for U_i in UserList:
                row = []
                for U_j in UserList:
                    if U_i.usr_id == U_j.usr_id:
                        row.append(0.0)
                    elif U_i.usr_id < U_j.usr_id:
                        row.append(__simil_UxU_Obj__(U_i,U_j))
                    else:
                        row.append(0.0)
                wr.writerow(row)
        return (__simil_UxU_ObjFull__(UserList,Y,PATH,True))


def __simil_UxU_Obj__(User_I,User_J):
    l_i = User_I.extractItem()
    l_j = User_J.extractItem()
    common_item = list(set(l_i).intersection(l_j))
    if common_item == []:
        return 0.0
    else:
        numeratore = 0.0
        denominatore = 0
        for item in common_item:
            t_i = filter( lambda x: x[1] == item, User_I.usr_rw)
            t_j = filter( lambda x: x[1] == item, User_J.usr_rw)
            membro_i = t_i[0][0] - User_I.average()
            membro_j = t_j[0][0] - User_J.average()
            numeratore += membro_i * membro_j
            denominatore += (membro_i**2) * (membro_j**2)


        if denominatore == 0:
            # print ('Warning denominatore 0 '+ str(len(common_item)))
            # if len(common_item) > 6:
            #     print User_I.usr_id
            #     print User_J.usr_id
            return 0.0
        else:
            return (numeratore/math.sqrt(denominatore))


