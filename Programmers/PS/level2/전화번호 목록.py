def solution(phone_book):
    h_map = dict()
    for phone in phone_book:
        h_map[phone] = h_map.get(phone, 0) + 1
    for phone in phone_book:
        tmp = ''
        for p in phone[:-1]:
            tmp += p
            if tmp in h_map:
                return False
    return True
            