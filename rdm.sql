DROP DATABASE IF EXISTS rdm;
CREATE DATABASE rdm;
USE rdm;

CREATE TABLE MUSICIEN(
 id_mus MEDIUMINT(6),
 nom VARCHAR(50),
 prenom VARCHAR(50),
 instrument VARCHAR(50),
 style_musical VARCHAR(255),
 estLive BIT(1),
 estDemat BIT(1),
 estDispo BIT(1),
 visuel VARCHAR(255),
CONSTRAINT pk__id_mus PRIMARY KEY(id_mus)
);

CREATE TABLE GROUPE(
 id_gro MEDIUMINT(6),
 nom_gro VARCHAR(255),
 style_musical VARCHAR(255),
 estLive BIT(1),
 estDemat BIT(1),
 visuel VARCHAR(255),
CONSTRAINT pk__id_gro PRIMARY KEY(id_gro)
);

CREATE TABLE CONTENU_MUSICIEN(
 id_con MEDIUMINT(6),
 url VARCHAR(255),
 id_mus MEDIUMINT(6),
CONSTRAINT pk__id_con PRIMARY KEY(id_con),
CONSTRAINT fk_id_mus FOREIGN KEY (id_mus) REFERENCES MUSICIEN(id_mus)
);

CREATE TABLE APPARTIENTA(
 id_mus MEDIUMINT(6),
 id_gro MEDIUMINT(6),
CONSTRAINT pk__id_mus_id_gro PRIMARY KEY(id_mus,id_gro),
CONSTRAINT fk_id_mus FOREIGN KEY (id_mus) REFERENCES MUSICIEN(id_mus),
CONSTRAINT fk_id_gro FOREIGN KEY (id_gro) REFERENCES GROUPE(id_gro)
);