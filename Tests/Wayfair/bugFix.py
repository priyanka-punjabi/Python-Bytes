"""
@author: Priyanka Punjabi
"""


def solution(S):
    occurrences = [0] * 26
    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
    print(occurrences)

    best_char = 'a'
    best_res = 0

    for i in range(0, 26):  # Modified Line
        if occurrences[i] > best_res:  # Modified Line
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char
