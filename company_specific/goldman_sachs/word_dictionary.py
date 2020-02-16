"""
Instructions to candidate.
 1) Given a a string of letters and a dictionary, the function longestWord should
    find the longest word or words in the dictionary that can be made from the letters
    Input: letters = "oet", dictionary = {"to","toe","toes"}
    Output: {"toe"}
    Only lowercase letters will occur in the dictionary and the letters
    The length of letters will be between 1 and 10 characters
    The solution should work well for a dictionary of over 100,000 words
 2) Run this code in the REPL to observe its behaviour. The
    execution entry point is main.
 3) Consider adding some additional tests in doTestsPass().
 4) Implement the longestWord() method correctly.
 5) If time permits, introduce '?' which can represent any letter.  "to?" could match to "toe", "ton" etc
"""

def longest_words(letters, dictionary):
    trie = {}
    for word in dictionary:
        cur = trie
        for l in word:
            if l not in cur:
                cur[l] = {}
            cur = cur[l]
        cur['$'] = True

    longest_words = []

    def find_longest(letters, cur, path):
        if '$' in cur:
            if len(longest_words) == 0 or len(longest_words[0]) == len(path):
                longest_words.append(''.join(path))
            elif len(path) > len(longest_words[0]):
                longest_words.clear()
                longest_words.append(''.join(path))
        for i, l in enumerate(letters):
            if l in cur:
                find_longest(letters[:i] + letters[i+1:], cur[l], path + [l])

    find_longest(letters, trie, [])
    return longest_words


if __name__ == '__main__':
    dictionary = {"to","toe","toes", 'eot'}
    print(longest_words('oet', dictionary))




