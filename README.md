<h1 align='center'> 
  Tweets Upload Simulation
</h1>

### Project Background

This project was inspired by twitter's usage of MySQL. When using MySQL as the back-end to pull multiple user's timeline, this tends to be slow. 
Redis, as a key-value DBMS can help solve this issue since key-value databases can scale with large amounts of data better than traditional relational database. 

### Prerequisites

- Have Redis and MySQL installed and the DBMSs running in the background: [https://redis.io/docs/getting-started/installation/](https://redis.io/docs/getting-started/installation/)\
     ↳ For Windows users, Memurai can be an alternative: [https://www.memurai.com/get-memurai](https://www.memurai.com/get-memurai)

- Have the Redis library in Python installed.

### Running the Comparison

The repository has 2 folders, one for datasets and the other housing the code. User can run the ```simulation_test.py``` file in the ```retrieval_simulation``` folder 
to see the time it takes to post tweets and retrieve timelines when using MySQL and Redis. 

### Significance of Project

This project was meant to show the feasibility of using a key-value store as a DBMS in certain circumstances such as high user volumes as in the case with twitter. As 
a company scales up and become more mainstream, the data it uses and retrieves goes up exponentially. Switching part of the database to a key-value DBMS is a popular
option.

 
