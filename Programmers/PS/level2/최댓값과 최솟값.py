def solution(s):
    nums = list(int(x) for x in s.split(' '))
    return "{} {}".format(min(nums), max(nums))