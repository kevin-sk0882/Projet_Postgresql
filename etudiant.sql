--  Créé l'utilisateur 'test' avec le mot de passe 'SuperNova' et donné lui les droits sauf pour la replication
--  Créé la base de données 'TestBDO' avec propriétaire 'test'
-- Executer ce script dans le QueryTool de TestBDO

CREATE TABLE test.etudiant(
    matricule SERIAL primary key,
    nom varchar(25) not null,
    prenom varchar(50) not null,
    age int DEFAULT 0,
    adresse varchar(255)
);