# robiya toq sonlar fun_odd
# akmalga 1-n gacha sonlarni print fun_print
# hushnud ngacha bolgan sonlarni teskari chiqarsin
# javlon 1-n gacha sonlarni 2marta chiqaridan
# adhamjonga juft sonlar fun_even

def teskari(n):
    return [i for i in range(n)][::-1]


def fun_print(n):
    return [i for i in range(1, n + 1)]


def fun_odd(nums):
    return [i for i in nums if i & 1]


def fun_even(n):
    if n % 2:
        return 'Juft Son'
    else:
        'Juft Son'


def from_one_to_n(n):
    return [i for i in range(1, n + 1)] * 2

# ctrl + k commit qilish
# ctrl + t gitdan olish
# ctrl + shift + k gitga yuborish