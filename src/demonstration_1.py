"""
You are given a non-empty list of words.

Write a function that returns the *k* most frequent elements.

The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.

Example 1:

```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2

Output:
["lambda", "school"]

Explanation:
"lambda" and "school" are the two most frequent words.
```

Example 2:

```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the",
    "the", "the", "cloudy", "is", "is"]
k = 4

Output:
["the", "is", "cloudy", "sky"]

Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```

Notes:

- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""


def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int
    Output:
    List[str]
    """
    # Your code here
    # 1. figure out how many times each word in `words` shows up
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # 2. takes words, starting with the word with highest frequency, until
    # we have `k` words
    # we can use Python's built in sort function to sort the contents of the
    # dictionary by the counts
    # in the callback, `x` is a key-value pair in the form of a tuple
    # res = sorted(word_counts, key=lambda k: (word_counts[k], k))
    # first sort by the counts, then by the words themselves if their counts are equal
    res = sorted(word_counts.items(), key=lambda kv: (-kv[1], kv[0]))
    # grab just the first elements from the tuples in `res`
    # return [t[0] for t in res[:k]]
    output = []
    for i in range(k):
        t = res[i]
        output.append(t[0])
    return output


print(top_k_frequent(["the", "sky", "is", "cloudy",
                      "the", "the", "the", "cloudy", "is", "is"], 4))
