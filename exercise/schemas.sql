-- Constraints in the `tubes.csv` file are:
  -- 1. Valid `tube_type`s are "Thermo" and "REMP".
  -- 2. Valid `tube_size`s are 50mL, 100mL, 150mL, and 200mL.

-- Constraints on the `readings.csv` file are:
  -- 1. All `tube_id`s should also appear in `tubes.csv`
  -- 2. Both concentration values should be non-negative

-- create `experiments.tubes` table
CREATE TABLE IF NOT EXISTS tubes (
  tube_id VARCHAR NOT NULL PRIMARY KEY,
  strain_id VARCHAR,
  tube_type VARCHAR NOT NULL CHECK(tube_type IN ('Thermo','REMP')),
  tube_size VARCHAR NOT NULL CHECK(tube_size IN ('50mL', '100mL', '150mL','200mL')),
  freezer VARCHAR,
  created_at DATETIME DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

-- create `experiments.readings` table
CREATE TABLE IF NOT EXISTS readings (
  reading_id VARCHAR NOT NULL PRIMARY KEY,
  tube_id VARCHAR NOT NULL, 
  lactate_concentration FLOAT CHECK (lactate_concentration >= 0),
  acetate_concentration FLOAT CHECK (acetate_concentration >= 0),
  created_at DATETIME DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),

  CONSTRAINT fk_tube_id
    FOREIGN KEY (tube_id)
    REFERENCES tubes (tube_id)
);

-- create `experiments.strains` table
CREATE TABLE IF NOT EXISTS strains (
  strain_id VARCHAR NOT NULL PRIMARY KEY,
  food_type VARCHAR,
  food_name VARCHAR, 
  food_production_source VARCHAR,
  food_retail_source VARCHAR,
  created_at DATETIME DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

