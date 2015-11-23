from GestioneInput import __initData, __addNote
from Object.ObjectUser import __WriteMatrixCF2__, __getMatrixCF2__, __getMatrixCF_TESTSET2__
from ObjectItem import __getMatrixCF_ITEM__, stampaItemCount,__listaItemEliminati__, __getMatrixCF_ITEM2__
from ObjectUser import __WriteMatrixCF__, __getMatrixCF__, __getMatrixCF_TESTSET__
from RecommenderSystem import __recSystemObjUxU__, ____recSystemObjUxUNextNeighbour__
from SimilarityUxU import __simil_UxU_ObjFull__, __simil_UxU_ObjFull2__, __simil_UxU_ObjProva__, pearson
from SimilarityIxI import __simil_IxI_ObjFull__, __simil_IxI_ObjFull2__

__author__ = 'matteo'


def main(nome,nTest=None,K_0=20,K_1=10,K_2=5,K_3=3,K_4=20,dataset='ml-100k',path='/home/matteo/Desktop/DataMining/ml-100k/',X=0,Y=0):

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

    PATH = __initData(path,nome,dataset,K_0,nTest)

    print PATH

    #__WriteMatrixCF__(0,path,PATH,X,Y)

    # Item = __getMatrixCF_ITEM__(PATH,X)
    # User = __getMatrixCF__(PATH)
    # UserTest = __getMatrixCF_TESTSET__(PATH)
    #
    # stampaItemCount(Item)
    #
    # Itemlist = __listaItemEliminati__(Item,5)
    # __WriteMatrixCF2__(K_0,path,PATH,X,Y,Itemlist)
    #
    # __WriteMatrixCF__(K_0,path,PATH,X,Y)

    Item2 = __getMatrixCF_ITEM2__(PATH,X)
    User2 = __getMatrixCF2__(PATH)
    UserTest2 = __getMatrixCF_TESTSET2__(PATH)

    #
    #
    Item = __getMatrixCF_ITEM__(PATH,X)
    User = __getMatrixCF__(PATH)
    UserTest = __getMatrixCF_TESTSET__(PATH)
    #




    print "----------------"
    #
    # SimMatrix = __simil_UxU_ObjFull__(User,K_4,Y,PATH,Written=True)
    #
    # __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,K_1,K_2,K_3))
    #
    # print "----------------"
    #
    # SimMatrix2 = __simil_UxU_ObjFull2__(User,1.5,Y,PATH,Written=True)
    #
    # __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix2,PATH,K_1,K_2,K_3))

    print "----------------"

    #__addNote(path,____recSystemObjUxUNextNeighbour__(User,UserTest,SimMatrix,PATH,K_1,K_2,K_3,20))




    print "----------------"

    SimMatrix = __simil_UxU_ObjFull__(User2,K_4,Y,PATH,Written=True)

    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,K_1,K_2,K_3))

    print "----------------"

    #SimMatrix2 = __simil_UxU_ObjFull2__(User2,1.5,Y,PATH,Written=True)

    #11__addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix2,PATH,K_1,K_2,K_3))

    print "----------------"

    #__addNote(path,____recSystemObjUxUNextNeighbour__(User,UserTest,SimMatrix,PATH,K_1,K_2,K_3,20))







if __name__ == "__main__":
    #K_0 = PERCENTUALE TEST SET
    #K_1 = VICINATO NEL RECCOMMANDER
    #K_2 = NUMERO DI OGGETTI DA ESTRARRE PER OGNI UTENTE NEL VICINATO
    #K_3 = NUMERO DI RACCOMANDAZIONI FINALE
    #K_4 = DIMENSIONE RIGA MATRICE DI SIMILARITA'
    main('FullData',9,K_0=20,K_1=4,K_2=4,K_3=2,K_4=0.9 ,dataset='ml-100k')



    #for k1 in range (1,16):
    #     for k2 in range (1,11):
    #for k3 in range(2,6):
        #main('FullData',9,K_0=20,K_1=4,K_2=4,K_3=k3,K_4=0.9 ,dataset='ml-100k')



