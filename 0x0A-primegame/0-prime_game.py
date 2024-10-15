#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Checks the winner of the game """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    num_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not num_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            num_filter[j] = False
    num_filter[0] = num_filter[1] = False
    san = 0
    for i in range(len(num_filter)):
        if num_filter[i]:
            san += 1
        num_filter[i] = san
    jel = 0
    for x in nums:
        jel += num_filter[x] % 2 == 1
    if jel * 2 == len(nums):
        return None
    if jel * 2 > len(nums):
        return "Maria"
    return "Ben"
