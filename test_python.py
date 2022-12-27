# robiya toq sonlar fun_odd
# akmalga 1-n gacha sonlarni print fun_print
# hushnud ngacha bolgan sonlarni teskari chiqarsin
# javlon 1-n gacha sonlarni 2marta chiqaridan
# adhamjonga juft sonlar fun_even


def fun_odd(nums):
    return [i for i in nums if i & 1]


def fun_even(n):
    if n % 2:
        return 'Juft Son'
    else:
        'Juft Son'
