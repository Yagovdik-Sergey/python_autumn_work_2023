nums_1 = [[3, 4, 6, 723], [1, 2], [134, 234, 34], [425355, 12356], [345, 3, 9], [2, 5, 6, 9, 7]]
nums_down = []
for k in nums_1:
    nums = sorted(k, reverse=True)
    nums_down.append(nums)
for i in nums_down:
    nums_down.sort(key=lambda x: (len("".join(map(str, x)))))
print(nums_down)
