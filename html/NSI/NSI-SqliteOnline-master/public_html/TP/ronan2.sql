
DROP TABLE IF EXISTS Pays;

CREATE TABLE Pays (
  Code TEXT PRIMARY KEY NOT NULL,
  Nom TEXT NOT NULL,
  Continent TEXT,
  Region TEXT NOT NULL,
  Superficie REAL NOT NULL,
  Population INT NOT NULL,
  EspeVie REAL,
  NomLocal TEXT NOT NULL,
  TypeGouvernance TEXT NOT NULL,
  ChefEtat TEXT DEFAULT NULL
);

