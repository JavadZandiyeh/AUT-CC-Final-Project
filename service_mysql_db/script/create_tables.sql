CREATE TABLE Coin (
  coin_name VARCHAR(100),
  time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  price FLOAT,
  PRIMARY KEY (coin_name, time_stamp)
);

CREATE TABLE CoinAlertSubscription (
  email VARCHAR(100),
  coin_name VARCHAR(100),
  difference_percentage INT,
  FOREIGN KEY (coin_name) REFERENCES Coin(coin_name),
  PRIMARY KEY (email, coin_name)
);