## Tweets Upload Simulation

### Project Background

This project was inspired by twitter's usage of MySQL. When using MySQL as the back-end to pull multiple user's timeline, this tends to be slow. 
Redis, as a key-value DBMS can help solve this issue since key-value databases can scale with large amounts of data better than traditional relational database. 

### Prerequisites

- Have Redis installed and the DBMS running in the background: ```https://redis.io/docs/getting-started/installation/```
‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ↳ For Windows users, Memurai can be an alternative: ```https://www.memurai.com/get-memurai```

- Have the Redis library in Python installed.

### Running the Comparison

The repository will have 2 folders, one using MySQL and the other using Redis. User can run the ```simulation_test.py``` file in each folder
to see the runtime of data retrieval by using a RDB and a KVDB respectively. 

 
