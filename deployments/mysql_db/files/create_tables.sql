CREATE TABLE IF NOT EXISTS Coin (
  coin_name VARCHAR(100),
  PRIMARY KEY (coin_name)
);

CREATE TABLE IF NOT EXISTS Prices (
  coin_name VARCHAR(100),
  time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  price FLOAT NOT NULL,
  FOREIGN KEY (coin_name) REFERENCES Coin(coin_name),
  PRIMARY KEY (coin_name, time_stamp)
);

CREATE TABLE IF NOT EXISTS AlertSubscriptions (
  email VARCHAR(100),
  coin_name VARCHAR(100),
  difference_percentage INT NOT NULL,
  FOREIGN KEY (coin_name) REFERENCES Coin(coin_name),
  PRIMARY KEY (email, coin_name)
);