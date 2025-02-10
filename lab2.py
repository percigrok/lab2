# 1 задание 9 вариант
# import itertools
#
# alhabet = "ABCDEXZ"
# s = 'XZ'
# s1 = 'ABCDE '
# ar = itertools.product(alhabet, repeat = 4 )
# arl = []
# for i in ar:
#     arl.append(list(i))
# count = 0
# for e in arl:
#     if e[0] in s and e[1] in s and e[2] in s1 and e[3] in s1:
#         count+=1
# print(count)

# 2
# x = 49**10 + 7**30 - 49
# s = ''
# while x != 0:
#     s += str(x % 7)
#     x //= 7
# s = s[::-1]
# print(s.count("6"))

#3
# for num in range(312614, 312652):
#     divisors = [i for i in range(1, num + 1) if num % i == 0]
#     if len(divisors) == 6:
#         print(*divisors)