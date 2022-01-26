


class Player:

    def __init__(self,pseudo,score):
        self._pseudoP=pseudo
        self._scoreP=score

    def getPseudoP(self):
        return self._pseudoP

    def getScoreP(self):
        return self._scoreP

    def afficherScore(self,cle):
        return self.getScoreP()[cle]

    def moyenneScore(self):
        moyenne=0
        for cle, valeur in self.getScoreP().items():
            moyenne=moyenne+valeur
        moyenne=moyenne/5
        return moyenne

    def totalScore(self):
        total=0
        for cle, valeur in self.getScoreP().items():
            total=total+valeur
        return total

    def meilleurScore(self):
        meilleurScore=0
        cleScore=0
        for cle, valeur in self.getScoreP().items():
            if valeur>meilleurScore:
                meilleurScore=valeur
                cleScore=cle
        print("le meilleur score est: ",meilleurScore, " sur la chanson: ", cleScore)

    def pireScore(self):
        pireScore=100
        cleScore=0
        for cle, valeur in self.getScoreP().items():
            if valeur<pireScore:
                pireScore=valeur
                cleScore=cle
        print("le pire score est: ",pireScore, " sur la chanson: ", cleScore)

    def ajouterScore(self,cle,score):
        self.getScoreP()[cle]=score
        print("A la cle ",cle," nous avons désormais ",score," points")




class Karaoke:

    def __init__(self,listJoueur,listChanson):
        self._listJoueurK=listJoueur
        self._listChansonK=listChanson

    def getJoueur(self):
        return self._listJoueurK
    
    def getChanson(self):
        return self._listChansonK

    def ajouterJoueur(self,joueur):
        self.getJoueur().append(joueur)
        print("joueur ajouter")

    def supprimerJoueur(self,joueur):
        self.getJoueur().remove(joueur)
        print("joueur supprimer")

    def meilleurScoreChanson(self,chanson):
        valeur=0
        plusGrandeValeur=0
        for i in range (len(self.getJoueur())):
            valeur=self.getJoueur()[i].afficherScore(chanson)
            if valeur>plusGrandeValeur:
                plusGrandeValeur=valeur
        print("Le meilleur score est: ",plusGrandeValeur)
        
    def meilleurScoreTotal(self):
        valeurScore=0
        plusGrandScore=0
        for i in range (len(self.getJoueur())):
            valeurScore=self.getJoueur()[i].totalScore()
            if valeurScore>plusGrandScore:
                plusGrandScore=valeurScore
        print("Le meilleur score général est: ",plusGrandScore)

    def meilleurMoyenne(self):
        moyennej=0
        plusGrandemoyenne=0
        for i in range (len(self.getJoueur())):
            moyennej=self.getJoueur()[i].moyenneScore()
            if moyennej>plusGrandemoyenne:
                plusGrandemoyenne=moyennej
        print("La meilleure moyenne est: ",plusGrandemoyenne)


scorebase={"j'aime":50, "nounours":80, "poisson":100, "verre":0, "singe":60}
scorebase2={"j'aime":50, "nounours":0, "poisson":50, "verre":90, "singe":70}
scorebase3={"j'aime":0, "nounours":100, "poisson":50, "verre":0, "singe":0}
j1= Player("bertrand",scorebase)
j2= Player("bertrand2",scorebase2)
j3= Player("bertrand3",scorebase3)

j1.moyenneScore()
j1.totalScore()
j1.meilleurScore()
j1.pireScore()
j1.ajouterScore(3,90)

listJoueur=[j1,j2]
listChanson=["j'aime","nounours","poisson","verre","singe"]
karaokeTest= Karaoke(listJoueur,listChanson)
karaokeTest.ajouterJoueur(j3)
print(karaokeTest.getJoueur())
karaokeTest.meilleurScoreChanson("j'aime")
karaokeTest.meilleurScoreTotal()
karaokeTest.meilleurMoyenne()
karaokeTest.supprimerJoueur(j3)
print(karaokeTest.getJoueur())
