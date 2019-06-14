Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(c) relies only on accessing an list element by index

2. What is the space complexity of your ring buffer's `append` function?
O(c) - once the list is created, its size does not change

3. What is the runtime complexity of your ring buffer's `get` method?
O(n) - my implementation iterates over every item to filter out None's

4. What is the space complexity of your ring buffer's `get` method?
O(n) - seems like the size of this result grows as n grows


5. What is the runtime complexity of the provided code in `names.py`?
O(n^2) or maybe O(n*m), but n and m are both 10,000. For each n, we iterate across the full list of m's.

6. What is the space complexity of the provided code in `names.py`?
Worst case seems to be O(n^2) here too, if we have a list of 10,000 duplicate names, we're going to have a list of n^2
duplicates.

7. What is the runtime complexity of your optimized code in `names.py`?
For the BinarySearchTree implementation, O(nlog(n)).
For the dictionary implementation, O(n)

8. What is the space complexity of your optimized code in `names.py`?
O(n) for both.
