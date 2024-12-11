def palindrome(sentence: str):
    isPalindrome = True
    sentence_lower = sentence.lower().replace(' ', '')
    index = 0
    endIndex = 0

    if len(sentence_lower) % 2 == 0:
        endIndex = int(len(sentence_lower) / 2)
    else:
        endIndex = int((len(sentence_lower) - 1) / 2)

    while index < endIndex:
        if sentence_lower[index] != sentence_lower[len(sentence_lower) - 1 - index]:
            isPalindrome = False
            break
        index += 1

    return isPalindrome


print(palindrome('anna'))

print(palindrome('abc'))

print(palindrome('Anna'))

print(palindrome('My gym'))
