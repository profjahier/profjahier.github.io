
DROP TABLE IF EXISTS "RelationLivreTheme";
CREATE TABLE IF NOT EXISTS "RelationLivreTheme" (
	"IdLivre"	INTEGER,
	"IdTheme"	INTEGER,
	FOREIGN KEY("IdLivre") REFERENCES "Livre",
	FOREIGN KEY("IdTheme") REFERENCES "Theme",
	PRIMARY KEY("IdLivre","IdTheme")
);
DROP TABLE IF EXISTS "Theme";
CREATE TABLE IF NOT EXISTS "Theme" (
	"IdTheme"	INTEGER,
	"Intitule"	TEXT,
	PRIMARY KEY("IdTheme")
);
DROP TABLE IF EXISTS "Livre";
CREATE TABLE IF NOT EXISTS "Livre" (
	"IdLivre"	INTEGER,
	"Titre"	TEXT,
	"IdAuteur"	INTEGER,
	"AnneePubli"	INTEGER,
	PRIMARY KEY("IdLivre"),
	FOREIGN KEY("IdAuteur") REFERENCES "Auteur"
);
DROP TABLE IF EXISTS "Auteur";
CREATE TABLE IF NOT EXISTS "Auteur" (
	"IdAuteur"	INTEGER,
	"NomAuteur"	TEXT,
	"PrenomAuteur"	TEXT,
	"IdLangue"	INTEGER,
	"AnneeNaissance"	INTEGER,
	FOREIGN KEY("IdLangue") REFERENCES "Langue",
	PRIMARY KEY("IdAuteur")
);
DROP TABLE IF EXISTS "Langue";
CREATE TABLE IF NOT EXISTS "Langue" (
	"IdLangue"	INTEGER,
	"Langue"	TEXT,
	PRIMARY KEY("IdLangue")
);
INSERT INTO "RelationLivreTheme" ("IdLivre","IdTheme") VALUES (1,2),
 (1,1),
 (1,3),
 (1,4),
 (2,1),
 (2,3),
 (3,1),
 (3,5),
 (4,2),
 (4,1),
 (4,4),
 (5,1),
 (5,4),
 (6,1),
 (6,3),
 (7,1),
 (7,3),
 (8,1),
 (8,6),
 (9,1),
 (10,1),
 (11,1),
 (11,4),
 (12,1),
 (12,3),
 (13,4),
 (13,8),
 (9,10),
 (10,10),
 (15,10),
 (14,1),
 (14,4),
 (15,1),
 (16,1),
 (16,9);
INSERT INTO "Theme" ("IdTheme","Intitule") VALUES (1,'Science-fiction'),
 (2,'Totalitarisme'),
 (3,'Anticipation'),
 (4,'Dystopie'),
 (5,'Economie'),
 (6,'Tragédie'),
 (7,'Uchronie'),
 (8,'Voyage dans le temps'),
 (9,'Aventure'),
 (10,'Intelligence artificielle');
INSERT INTO "Livre" ("IdLivre","Titre","IdAuteur","AnneePubli") VALUES (1,'1984',1,1949),
 (2,'Dune',2,1965),
 (3,'Fondation',3,1951),
 (4,'Le meilleur des mondes',4,1931),
 (5,'Fahrenheit 451',5,1953),
 (6,'Ubik',6,1969),
 (7,'Chroniques martiennes',5,1950),
 (8,'La nuit des temps',7,1968),
 (9,'Blade Runner',6,1968),
 (10,'Les Robots',3,1950),
 (11,'Ravage',7,1943),
 (12,'Le Maître du Haut Château',6,1962),
 (13,'La fin de l''éternité',3,1955),
 (14,'La planete des singes',8,1963),
 (15,'Le monde des A',9,1945),
 (16,'De la Terre a la Lune',10,1865);
INSERT INTO "Auteur" ("IdAuteur","NomAuteur","PrenomAuteur","IdLangue","AnneeNaissance") VALUES (1,'Orwell','George',1,1903),
 (2,'Herbert','Frank',1,1920),
 (3,'Asimov','Isaac',1,1920),
 (4,'Huxley','Aldous',1,1894),
 (5,'Bradbury','Ray',1,1920),
 (6,'K. Dick','Philip',1,1928),
 (7,'Barjavel','René',2,1911),
 (8,'Boulle','Pierre',2,1912),
 (9,'Van Vogt','Alfred Elton',1,1912),
 (10,'Verne','Jules',2,1828);
INSERT INTO "Langue" ("IdLangue","Langue") VALUES (1,'Anglais'),
 (2,'Français');
 
 select * from livre;select * from auteur;select * from theme;select * from langue;select * from Relationlivretheme;
 
 SELECT DISTINCT
Titre as "Livre", NomAuteur as "Nom", PrenomAuteur as "Prénom", AnneeNaissance as "Né en", Langue, AnneePubli as "Publié en"
FROM RelationLivreTheme
JOIN Livre ON Livre.IdLivre = RelationLivreTheme.IdLivre
JOIN Auteur ON Auteur.IdAuteur = Livre.IdAuteur
JOIN Langue ON Langue.IdLangue = Auteur.IdLangue
ORDER BY Titre;
