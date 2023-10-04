lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
capital_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def code(string, n):
    cypher = ""
    for x in string:
        if x in lowercase_letters:
            ind = lowercase_letters.index(x) % len(lowercase_letters)
            cypher += lowercase_letters[(ind + n) % len(lowercase_letters)]
        elif x in capital_letters:
            ind = capital_letters.index(x) % len(capital_letters)
            cypher += capital_letters[(ind + n) % len(capital_letters)]
        else:
            cypher += x
    return cypher