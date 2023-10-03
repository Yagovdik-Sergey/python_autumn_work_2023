a = 'abcdefghijklmnopqrstuvwxyz'


def code(string, n):
    cypher = ''
    for i in string:
        ind = a.find(i)
        new_ind = ind + n
        if i in a:
            cypher += a[new_ind]
        else:
            cypher += i
    return cypher
