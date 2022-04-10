from os import system
import psycopg2

host = "localhost"
user =  "test"
password = "SuperNova"
db = "TestBDO"

def verifier(critere: str="n"):
    if critere[0].lower() == "o":
        return True
    return False

def connexion():
    return psycopg2.connect(host="localhost", database="TestBDO", user="test", password="SuperNova")

def insert(etudiant = {}):
    c = connexion()
    if c is not None:
        print("connexion reussi")
        system("pause")
        curseur = c.cursor()
        try:
            curseur.execute("insert into etudiant(nom, prenom, age, adresse) \
            values('%s','%s',%i,'%s')" % (etudiant["nom"], etudiant["prenom"], etudiant["age"], etudiant["adresse"]))
            c.commit()
            print("Insertion de %s %s %ians %s réussie..." % (etudiant["nom"], etudiant["prenom"], etudiant["age"], etudiant["adresse"]))
        except:
            print("La requête a rencontré des problèmes !")
        c.close()
    else:
        print("Erreur de connexion")
    input()

def select(colonnes: str='*'):
    c = connexion()
    curseur = c.cursor()
    if colonnes == "":
        colonnes = "*"
    try:
        curseur.execute("select %s from etudiant order by matricule asc" % colonnes)
    except:
        print("La requête a rencontré des problèmes !")
        return
    ligne = curseur.fetchone()
    print("--------------------- Résultat du SELECT ----------------")
    while ligne:
        for colonne in ligne:
            print(colonne, end='  ')
        print()
        ligne = curseur.fetchone()
    print("----------------------------------------------------------\n")
    curseur.close()
    c.close()
    input()

def delete(matricule: int):
    c = connexion()
    curseur = c.cursor()
    try:
        curseur.execute("delete from etudiant where matricule=%i" % matricule)
        if verifier(input("Voulez-vous vraiment supprimer cet etudiant ?[O/N]: ")):
            c.commit()
            print("Suppression réussi !", end='')
        else:
            c.rollback()
            print("Suppression annulée", end='')
    except:
        print("La requête a rencontré des problèmes !",end='')
    input()

def update(matricule: int, etudiant = {}):
    c = connexion()
    curseur = c.cursor()
    try:
        curseur.execute("update etudiant set nom = '%s' where matricule = %i" % (etudiant["nom"],matricule))
        curseur.execute("update etudiant set prenom = '%s' where matricule = %i" % (etudiant["prenom"],matricule))
        curseur.execute("update etudiant set age = %i where matricule = %i" % (etudiant["age"],matricule))
        curseur.execute("update etudiant set adresse = '%s' where matricule = %i" % (etudiant["adresse"],matricule))
        c.commit()
        print("Mise à jour réussi !")
    except:
        print("La requête a rencontré des problèmes !")
    input()