"""
You are given a non-empty list of words.
​
Write a function that returns the *k* most frequent elements.
​
The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.
​
Example 1:
​
```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2
​
Output:
["lambda", "school"]
    2         2
Explanation:
"lambda" and "school" are the two most frequent words.
```
​
Example 2:
​
```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4
​
Output:
["the", "is", "cloudy", "sky"]
   4     3       2        1
Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```
​
Notes:
​
- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int
​
    Output:
    List[str]
    """
    # Your code here
    # we want to figure out the number of occurrences of each word 
    # in the input list 
    word_occurrences = {}    
    # use a hash table to count the occurrence of words in the input list 
    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1
​
    # we could sort the words by their number of occurrences 
    # in the lambda function, x is the key of the 
    # we can have our lambda function return a tuple to represent 
    # the priority for how we want to sort 
    sorted_words = sorted(word_occurrences, key=lambda k: (-word_occurrences[k], k))
​
    # grab the top k words 
    return sorted_words[:k]
​
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
print(top_k_frequent(words, 4))
​
words = ["lambda", "achool", "rules", "lambda", "achool", "rocks"]
print(top_k_frequent(words, 2))
