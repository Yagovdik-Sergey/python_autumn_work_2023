from collections import OrderedDict
sentence = input()
print(' '.join(OrderedDict((i, i) for i in sentence.split()).keys()))