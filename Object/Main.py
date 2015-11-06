from GestioneInput import __initData, __addNote
from Object.ObjectItem import __getMatrixCF_ITEM__
from Object.ObjectUser import __WriteMatrixCF__, __getMatrixCF__, __getMatrixCF_TESTSET__
from Object.RecommenderSystem import __recSystemObjIxI__, __recSystemObjUxU__
from Object.SimilarityUxU import __simil_UxU_ObjFull__
from SimilarityIxI import __simil_IxI_ObjFull__

__author__ = 'matteo'


def main(nome,test,nTest=None,dataset='MovieLens',path='/home/matteo/Desktop/DataMining/ml-100k/',X=0,Y=0):

    if dataset == 'MovieLens':
        path='/home/matteo/Desktop/DataMining/ml-100k/'
        X=1682
        Y=943
    elif dataset == 'yelp':
        path='/home/matteo/Desktop/DataMining/yelp_dataset_academic/'
        X=13490
        Y=130873

    PATH = __initData(path,nome,dataset,test,nTest)

    print PATH
    #__addNote(path,'prova note')





    __WriteMatrixCF__(test,path,PATH,X,Y)
    User = __getMatrixCF__(PATH)
    UserTest = __getMatrixCF_TESTSET__(PATH)
    #
    #
    SimMatrix = __simil_UxU_ObjFull__(User,Y,PATH,Written=False)
    # print "ok"

    __addNote(path,__recSystemObjUxU__(test,User,UserTest,SimMatrix,Y,PATH))

    Item = __getMatrixCF_ITEM__(PATH,X)

    SimiliIxI = __simil_IxI_ObjFull__(Item,X,PATH,Written=False)

    __addNote(path,__recSystemObjIxI__(test,User,UserTest,Item,SimiliIxI,Y,PATH))






    # with open (path+'UtentixNrecensioni','w') as URP:
    #     wr1 = csv.writer(URP, dialect='excel')
    #     for u in User:
    #         print ('User : '+str(u.usr_id)+ ' Numero Recensioni : ' + str(u.rw_count))
    #         wr1.writerow([u.usr_id,u.rw_count])

    #print (__simil_UxU_Obj__(User[7],User[643]))
    # print User[0].user_rw
    # print User[2].user_rw

   # print len(Mat[1])

    #Matrix = __getData__(test, path, PATH,X,Y, False)
    #print __ReferenceRankig__(Matrix)

    #SimilMatrixUxU = __similUxU__(Matrix,PATH,Y,False)
    #__UserRatingPrediction__(6,PATH,Matrix,SimilMatrixUxU)
    #__addNote(path,__RMSE_MAE__(PATH))

    #SimilMatrixIxI = __similIxI__(Matrix,PATH,X,True)
    #__addNote(path,__ItemRatingPrediction__(10,PATH,Matrix,SimilMatrixIxI))

    #res = __UserRatingPrediction__(6,PATH,Matrix,SimilMatrix)

    #TODO: aggiungere nei log le misurazioni!
    #__RMSE_MAE__(PATH)



    #print __UsagePredictionCFPROVA__(15,PATH,Matrix,SimilMatrix)




if __name__ == "__main__":
    main('PROVA_OBJ',30,11)