def test_is_palindrome():
    assert is_palindrome(45) == False
    assert is_palindrome(555) == True
    assert is_palindrome(4554) == True
    assert is_palindrome(1221) == True

def is_palindrome(n):
    '''
    varifica daca numarule este palindrom
    :param n: natural
    :return: True sau False
    '''
    oglindit = 0
    copie = n
    while copie !=0:
        oglindit = oglindit*10 + copie %10
        copie = copie//10
    if oglindit == n:
        return True
    else:
        return False

def is_prime(n):
    prim = True
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            prim = False
    return prim


def get_largest_prime_below(n):
    '''
    Determina cel mai mare numar prim mai mic decat n
    :param n: intreg
<<<<<<< HEAD
    :return: cel mai mare numar prim mai mic decat  n
=======
    :return: cel mai mare numar prim mai mic decat n
    '''
    for i in range(n, 2, -1):
        check = is_prime(i)
        if check:
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(1) is None
    assert get_largest_prime_below(2) is None
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(100) == 97


def get_n_choose_k(n, k):
    '''
    Calculeaza combinari de n luate cate k
    :param n: natural
    :param k: natural
    :return: rezultatul combinarilor de n luate cate k
    '''
    n_factorial = 1
    k_factorial = 1
    dif_factorial = 1
    if k == 0:
        return 1
    for i in range(2, n + 1):
        n_factorial = n_factorial * i
    for i in range(2, k + 1):
        k_factorial = k_factorial * i
    for i in range(2, n - k + 1):
        dif_factorial = dif_factorial * i
    return int(n_factorial / (k_factorial * dif_factorial))


def test_get_n_choose_k():
    assert get_n_choose_k(5, 0) == 1
    assert get_n_choose_k(52, 5) == 2598960
    assert get_n_choose_k(10, 2) == 45


def main():
    test_is_palindrome()
    test_get_largest_prime_below()
    test_get_largest_prime_below()
    while True:
        print('1.Cel mai mare numar prim mai mic decat un numar ales')
        print('2.Calculeaza combinari de n luate cate k')
        print("3.Verifica daca un numar este palindrom")
        print('3.Exit')
        optiune = input('Alege optiune:')
        if optiune == '1':
            numar = int(input('Alege numar:'))
            c = get_largest_prime_below(numar)
            print(f'Cel mai mare numar prim mai mic decat numarul ales este:{c}')
        elif optiune == '2':
            n = int(input('Introdu valoare pentru  n:'))
            k = int(input('Introdu valoare pentru k:'))
            rezultat = get_n_choose_k(n, k)
            print(f'Rezultatul operatiei combinari de n luate cate k este:{rezultat}')
        elif optiune == '3':
            numar = int(input("Alege numar:"))
            if is_palindrome(numar) == True:
                print("Numarul este palindrom")
            else:
                print("Numarul nu este palindrom")
        else:
            print('Optiune invalida')


main()
