def s(n: int) -> int:
    if n <= 9:
        return n
    else:
        left_over = n
        number_string = ''
        while left_over > 9:
            number_string = '9' + number_string
            left_over -= 9
        number_string = str(left_over) + number_string
        return int(number_string)

def S(k: int) -> int:
    S_k = [0]
    for i in range(1, k + 1):
        S_k.append(S_k[i - 1] + s(i))
    return S_k

def f_n(n: int) -> int:
    f_n = [0, 1]
    for i in range(2, n + 1):
        f_n.append(f_n[i - 1] + f_n[i - 2])
    return f_n


if __name__ == '__main__':
    n = 90
    print(f_n(n))
