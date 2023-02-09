def solution(numbers):
    return [is_poss(n) for n in numbers]


def is_poss(n):
    digits = ''
    while n:
        n, res = divmod(n, 2)
        digits = str(res) + digits

    d_len = len(digits)
    len_check = 2
    while d_len >= len_check:
        len_check <<= 1
    len_check -= 1
    digits = digits.rjust(len_check, '0')
    c_idx = len_check>>1

    return 1 if is_center_one(c_idx, digits) else 0 


def is_center_one(c_idx, p_digits):
    if not c_idx:  # leaf node
        return p_digits[c_idx]

    left = is_center_one(c_idx>>1, p_digits[:c_idx])
    right = is_center_one(c_idx>>1, p_digits[-c_idx:])
    if not left or not right:
        return False

    if p_digits[c_idx] == '0':
        if left == '0' and right =='0':
            return '0'
        else:
            return False
    return '1'
