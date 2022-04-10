from Connexion import *
from os import system

system("cls")
print("\t\t::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\t\t:::::::::::::::::::::::: BONJOUR TOUT LE MONDE :::::::::::::::::::::::::")
print("\t\t::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("\n\t\t\t Ceci est un petit programme PL/Python avec Postgresql !!!\n")
system("pause")
while True:
    system("cls")
    print("\t\t++++++++++++++++++++++++++ MENU PRINCIPAL ++++++++++++++++++++++++")
    print("\t\t\t1- La liste des etudiants")
    print("\t\t\t2- Enregistrer un etudiant")
    print("\t\t\t3- Mettre à jour les infos d'un etudiant")
    print("\t\t\t4- Supprimer un etudiant")
    print("\t\t\t0- Quitter")
    print("\t\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    choix = input("Faites votre choix: ")
    while choix not in ("0","1","2","3","4"):
        system("cls")
        print("Saisie incorrect - Reéssayez !!!")
        system("pause")
        system("cls")
        print("\t\t++++++++++++++++++++++++++ MENU PRINCIPAL ++++++++++++++++++++++++")
        print("\t\t\t1- La liste des etudiants")
        print("\t\t\t2- Enregistrer un etudiant")
        print("\t\t\t3- Mettre à jour les infos d'un etudiant")
        print("\t\t\t4- Supprimer un etudiant")
        print("\t\t\t0- Quitter")
        print("\t\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        choix = input("Faites votre choix: ")
    if choix == "1":
        system("cls")
        colonne = input("Entrer la liste des colonnes à selectionner separé par de ',': ")
        select(colonne)
    elif choix == "2":
        system("cls")
        etudiant = {}
        try:
            etudiant["nom"] = input("Entrer le nom: ")
            etudiant["prenom"] = input("Entrer le prenom: ")
            etudiant["age"] = int(input("Entrer son age: "))
            etudiant["adresse"] = input("Entrer son adresse: ")
        except:
            print("Entrer incorrect !!!")
            continue
        insert(etudiant)
    elif choix == "3":
        system("cls")
        select()
        etudiant = {}
        try:
            matricule = int(input("Entrer le matricule de l'etudiant selectionné: "))
            system("cls")
            etudiant["nom"] = input("Entrer le nouveau nom: ")
            etudiant["prenom"] = input("Entrer le prenom: ")
            etudiant["age"] = int(input("Entrer son age: "))
            etudiant["adresse"] = input("Entrer son adresse: ")
            update(matricule, etudiant)
        except:
            print("Entrer incorrect !!!")
            system("pause")
            continue
    elif choix == "4":
        system("cls")
        select()
        etudiant = {}
        try:
            matricule = int(input("Entrer le matricule de l'etudiant selectionné: "))
            delete(matricule)
        except:
            print("Entrer incorrect !!!")
            continue
    elif choix == "0":
        break
system("cls")
print("Au revoir ...")