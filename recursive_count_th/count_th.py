'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
letters = 'abthabthabth'

def count_th(word):
    # TBC
    th_count = 0
    # if the length of word is less than 2, return 0
    if len(word) < 2:
        return 0
    # if the word itself is 'th', return 1
    if word == 'th':
        return 1
    # if the length of the word is 2 and it isn't 'th', return 0
    if len(word) == 2 and 'th' not in word:
        return 0
    # if two subsequent characters = 'th', recurse and count
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

print(count_th(letters))
