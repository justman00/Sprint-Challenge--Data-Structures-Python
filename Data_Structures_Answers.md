Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   it is constant O(1)

2) What is the space complexity of your ring buffer's `append` function?
   I dont use any space, thus it is 0

3) What is the runtime complexity of your ring buffer's `get` method?
   it is O(n) - linear because I move through the elements and filter out the ones that are None

4) What is the space complexity of your ring buffer's `get` method?
   its linear - O(n), because I return a list

5. What is the runtime complexity of the provided code in `names.py`?
   O(n^2)

6. What is the space complexity of the provided code in `names.py`?
   its also linear, since they just use lists

7. What is the runtime complexity of your optimized code in `names.py`?
   linear

8. What is the space complexity of your optimized code in `names.py`?
   same as before, but I use sets and lists, which makes it linear
