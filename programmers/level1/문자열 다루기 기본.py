def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            if isinstance(int(s), int):
                return True
        except:
            return False
    else:
        return False