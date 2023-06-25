# MongoDB-Hadoop-SON-Algorithm
This repository focuses on utilizing MongoDB data in Hadoop by connecting the two and performing the SON algorithm for frequent itemset mining.
Each document in MongoDB is treated as a transaction, and the algorithm is applied to chunks of data in parallel. 
The steps involve identifying frequent itemsets using a simple randomized algorithm, generating candidate itemsets through reduce tasks, counting occurrences of candidate itemsets, and aggregating the results. 
The output includes frequent itemsets with support exceeding a specified threshold.
