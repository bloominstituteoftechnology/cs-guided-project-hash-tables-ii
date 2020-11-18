"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""


def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str

    Output:
    str

    1 - Init a hash table for counts
    2 - Sort by the counts in descending order
    3 - We need to reconstruct the output string from the frequency of each letter
    """
    letter_counts = {}

    for letter in s:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    res = sorted(letter_counts.items(), key=lambda kv: (-kv[1]))

    # iterate through `res` & append each letter to a list `count` times
    # alt:
    # word = [letter * count for letter, count in res]
    word = []
    for letter, count in res:
        word.append(letter * count)

    # now that the `word` list contains all the necessary characters, join them into a string
    return ''.join(word)


print(frequency_sort('Bbcc'))
