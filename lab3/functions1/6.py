def rev(sentence):
    words = sentence.split()
    revSentence = ' '.join(reversed(words))
    return revSentence


a = input()
result = rev(a)
print(result)
