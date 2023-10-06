DNA = "АГЦТГАТЦ"
res = ''
for ind, ch in enumerate(DNA[:-1]):
    if ord(ch) == 1040 and ord(DNA[ind + 1]) == 1043 or ord(ch) == 1043 and ord(DNA[ind + 1]) == 1040:
        print(ind, ch)
        # for i in range(0, len(DNA), 2):
        #     res += DNA[i:i + 2][::-1]
        #     print(res)


# tran_table = DNA.maketrans("АГ", "ГА")
# DNA.translate(tran_table)
# print(DNA.translate(tran_table))


# print(ord('А')) 1040
# print(ord('Г')) 1043