sentence = str(input())
first_longest_word = max(sentence.split(), key=len)
print(first_longest_word)