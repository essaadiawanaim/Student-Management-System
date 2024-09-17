import mysql.connector
# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="enregistrer"
)
cur = cnx.cursor()
''' 
# creation de la table  compte pour stocker les données entrer dans le formulaire d'inscription
create_table1 = """
CREATE TABLE compte (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  cne VARCHAR(30),
  prenom VARCHAR(50),
  nom VARCHAR(20),
  date_naissance DATE,
  filiere VARCHAR(50),
  sexe varchar(15),
  telephone VARCHAR(50),
  nationalite VARCHAR(20),
  address VARCHAR(50),
  annee_bac date,
  email VARCHAR(30),
  question VARCHAR(40),
  reponse VARCHAR(30),
  password VARCHAR(20)
);
"""
cur.execute(create_table1)


# creation de la table inscritetudiant pour stocker les données de la listes(où tables qui apparaitre dans la fenetre ListEtudiant)
create_table2 = """
CREATE TABLE inscritetudiant (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  sexe varchar(15) NOT NULL,
  contact VARCHAR(20) NOT NULL,
  filiere VARCHAR(50) NOT NULL,
  ville VARCHAR(50) NOT NULL
)
"""
cur.execute(create_table2)
'''

# Commit the changes
cnx.commit()
# Close the cursor and connection
cur.close()
cnx.close()
