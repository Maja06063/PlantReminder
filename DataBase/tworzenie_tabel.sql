USE plantreminderdb;

DROP TABLE SpecialEvent;
DROP TABLE Plants;
DROP TABLE Species;
DROP TABLE UserName;

CREATE TABLE UserName(
    login varchar(255) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    e_mail varchar(255) NOT NULL
);

CREATE TABLE Species(
    species_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    watering_period int NOT NULL,
    fertilization_period int NOT NULL,
    light int NOT NULL
);

CREATE TABLE Plants(
    plant_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    login varchar(255) NOT NULL,
    plant_species int NOT NULL,
    plant_name varchar(20),
    watering_period int,
    fertilization_period int,
    light int,
    plant_description varchar(100),
    last_watering_date date NOT NULL,
    last_fertilization_date date NOT NULL,

    FOREIGN KEY (login) REFERENCES UserName(login),
    FOREIGN KEY (plant_species) REFERENCES Species(species_id)
);

CREATE TABLE SpecialEvent(
    special_event_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    plant_id int NOT NULL,
    event_name varchar(255) NOT NULL,
    event_description varchar(1000),
    event_date date NOT NULL,

    FOREIGN KEY (plant_id) REFERENCES Plants(plant_id)
);
