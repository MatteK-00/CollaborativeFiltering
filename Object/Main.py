from GestioneInput import __initData, __addNote
from ObjectItem import __getMatrixCF_ITEM__, stampaItemCount,__listaItemEliminati__
from ObjectUser import __WriteMatrixCF__, __getMatrixCF__, __getMatrixCF_TESTSET__
from RecommenderSystem import __recSystemObjIxI__, __recSystemObjUxU__
from SimilarityUxU import __simil_UxU_ObjFull__, __simil_UxU_ObjFull2__
from SimilarityIxI import __simil_IxI_ObjFull__, __simil_IxI_ObjFull2__

__author__ = 'matteo'


def main(nome,test,nTest=None,dataset='ml-100k',path='/home/matteo/Desktop/DataMining/ml-100k/',X=0,Y=0):

    if dataset == 'ml-100k':
        path='/home/matteo/Desktop/DataMining/ml-100k/'
        X=1682
        Y=943
    elif dataset == 'ml-1m':
        path='/home/matteo/Desktop/DataMining/ml-1m/'
        X=3952
        Y=6040
    elif dataset == 'yelp':
        path='/home/matteo/Desktop/DataMining/yelp_dataset_academic/'
        X=13490
        Y=130873

    PATH = __initData(path,nome,dataset,test,nTest)

    print PATH
    #__addNote(path,'prova note')





    __WriteMatrixCF__(test,path,PATH,X,Y)
    Item = __getMatrixCF_ITEM__(PATH,X)
    User = __getMatrixCF__(PATH)
    UserTest = __getMatrixCF_TESTSET__(PATH)
    #
    # print "----------------"
    #
    # SimMatrix = __simil_UxU_ObjFull__(User,test,Y,PATH,Written=False)
    #
    #
    # __addNote(path,__recSystemObjUxU__(test,User,UserTest,SimMatrix,Y,PATH))
    #
    # print "----------------"
    #
    # SimiliIxI = __simil_IxI_ObjFull__(Item,test,X,PATH,Written=False)
    #
    # __addNote(path,__recSystemObjIxI__(test,User,UserTest,Item,SimiliIxI,Y,PATH))
    #
    #
    # print "----------------"
    #
    SimiliIxI2 = __simil_IxI_ObjFull2__(Item,test,X,PATH,Written=False)
    
    __addNote(path,__recSystemObjIxI__(test,User,UserTest,Item,SimiliIxI2,Y,PATH))


    #calcolo con item in meno del dataset su base percentile
    # __WriteMatrixCF__(test,path,PATH,X,Y)
    # Item = __getMatrixCF_ITEM__(PATH,X)

    # Itemlist = __listaItemEliminati__(Item,13)
    # __WriteMatrixCF__(test,path,PATH,X,Y,Itemlist)

    # Item = __getMatrixCF_ITEM__(PATH,X)
    # User = __getMatrixCF__(PATH)
    # UserTest = __getMatrixCF_TESTSET__(PATH)

    print "----------------"

    # SimMatrix = __simil_UxU_ObjFull__(User,test,Y,PATH,Written=False)
    # __addNote(path,__recSystemObjUxU__(test,User,UserTest,SimMatrix,Y,PATH))

    # print "----------------"

    # SimMatrix = __simil_UxU_ObjFull2__(User,test,Y,PATH,Written=False)
    # __addNote(path,__recSystemObjUxU__(test,User,UserTest,SimMatrix,Y,PATH))

    # print "----------------"

    # SimiliIxI = __simil_IxI_ObjFull__(Item,test,X,PATH,Written=False)
    # __addNote(path,__recSystemObjIxI__(test,User,UserTest,Item,SimiliIxI,Y,PATH))

    # print "----------------"

    #SimiliIxI2 = __simil_IxI_ObjFull2__(Item,test,X,PATH,Written=False)
    #__addNote(path,__recSystemObjIxI__(test,User,UserTest,Item,SimiliIxI2,Y,PATH))



#if __name__ == "__main__":
    #main('TEST_FullData',10,0,dataset='ml-1m')