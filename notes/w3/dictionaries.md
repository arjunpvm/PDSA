# Dictionaries
***
###### **Dictionary is the python specific implementation of the hash table**
In an array A given i we can find A[i] in constant time. So its keys are mapped to {0, 1, ..., n-1}

Given an key it converts it to an offset i

### Hash Function
* h : S --> X , maps a set of values S to a small range of integers {0, 1, ..., n-1}
* Typically |S| >> |X| so there will be collisions
* SHA256 is industry standard for hashing whose range is 256 bits
* a good hash fuction minimizes the no of collisions
* it is used to hash large files to avoid duplicates in cloud storage

