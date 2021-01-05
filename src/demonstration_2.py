"""
Given a string, sort it in decreasing order based on the frequency of characters.
​
Example 1:
​
```plaintext
Input:
"free"
​
{
    'f': 1,
    'r': 1,
    'e': 2,
}
​
Output:
"eefr"
​
Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```
​
Example 2:
​
```plaintext
Input:
"dddbbb"
​
Output:
"dddbbb"
​
Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```
​
Example 3:
​
```plaintext
Input:
"Bbcc"
​
Output:
"ccBb"
​
Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
​
from collections import Counter
​
# def frequency_sort(s: str) -> str:
#     counts = Counter(s)
​
#     letter_frequencies = counts.most_common()
​
#     return ''.join(letter * freq for letter, freq in letter_frequencies) 
​
def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str
​
    Output:
    str
    """
    # Your code here
    # we want to count the number of occurrences of individual letters 
    # in the input word 
    letter_occurrences = {}
​
    for letter in s:
        if letter in letter_occurrences:
            letter_occurrences[letter] += 1
        else:
            letter_occurrences[letter] = 1
​
    letter_occurrences = letter_occurrences.items()
​
    # we want to reconstruct the input word with letters that show up more 
    # frequently ordered first 
    sorted_letters = sorted(letter_occurrences, key=lambda t: -t[1])
    # [('e', 2), ('f', 1), ('r', 1)]
​
    # we want to take the letters in `sorted_letters` and construct a string out
    # of them 
    # construct the final string 
    # using a comprehension
    # return ''.join(letter * freq for letter, freq in sorted_letters)
​
    final_string = ''
​
    for letter, freq in sorted_letters:
        final_string += (letter * freq)
​
    return final_string
​
word = "free"
print(frequency_sort(word))
​
word = "Bbcc"
print(frequency_sort(word))