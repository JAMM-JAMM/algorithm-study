def solution(nums):
    p_dict = dict()
    for num in nums:
        p_dict[num] = p_dict.get(num, 0) + 1
    if len(p_dict.keys()) >= (len(nums) // 2):
        return len(nums) // 2
    else:
        return len(p_dict.keys())
    