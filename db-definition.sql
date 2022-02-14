
--This db definition only will save the 
--Stream of the data from the order book
--And save it persistent on a data base.
CREATE TABLE order_book (
    time timestamp,
    json text
);
