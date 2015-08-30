import csv
import heapq
import math

__author__ = 'matteo'





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


def __ItemRatingPrediction__(k,PATH,Matrix,SimilMatrix):
    res = []
    usersToTest = []
    itemsForUser = []
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

    resultList = []
    for u in usersToTest:
        itemList = []
        for j in range(0,len(Matrix[0])):
            if Matrix[u][j] != 0:
                temp = []
                for sim in range(0,len(SimilMatrix[j])):
                    if Matrix[u][sim] == 0:
                        temp.append((SimilMatrix[j][sim],sim))

                simil_j=heapq.nlargest(k,temp)
                somma = 0.0
                counter = 0
                for item in simil_j:
                    somma += float(item[0]) * (Matrix[u][j])
                    counter += 1

                itemList.append(((somma/counter),j))


        resultList.append((u,heapq.nlargest(k,itemList)))

    rankT = (heapq.nlargest(k,resultList))
    rank = []
    for r in rankT:
        rank.append(r[1])


    with open (PATH+'ItemRatingPrediction','w') as IRP:
        wr1 = csv.writer(IRP, dialect='excel')
        for ifu in itemsForUser:
            for iL in rank:
                TP = FN = FP = TN = 0
                if ifu[0] == iL[0]:
                    for it1 in iL[1]:
                        if it1 in ifu[1]:
                            TP += 1
                        else:
                            FN += 1
                    for it2 in ifu[1]:
                        if it2 in iL[1]:
                            FP += 1
                        else:
                            TN += 1

                wr1.writerow[ifu[0],'TP = '+str(TP) +' FN = '+str(FN)+' FP = '+str(FP)+' TN = '+str(TN),iL[0], ifu[0]]
                resP = [TP,FN,FP,TN]
                res.append(resP)

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


    IRP.close()
    testLine.close()


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
        return sol
        #URP.write(sol)

