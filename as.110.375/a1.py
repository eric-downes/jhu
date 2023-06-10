from string import ascii_lowercase as ALPHABET

import numpy as np

def gcd(i:int, j:int, v:bool = True):
    sm, big = sorted((i, j))
    while sm:
        if v: print(f'small={sm}, big={big}')
        big, sm = (sm, big % sm)
    return big

def ord_p(n:int, p:int):
    if p == 1: return 0
    if p <= 0: raise ValueError(f'p must be positive: {p}')
    for k in range(n):
        n, r = divmod(n, p)
        if r: return k
    raise ValueError(f'impossible! :(')

def pow_sqmul(a:int, x:int, n:int, v:bool = False) -> int:
    b = 1
    for _ in range(x):
        x, r = divmod(x, 2)
        if r: b = b * a % n
        if v: print(f'value={b}, exponent={x}')
        if x: a = a * a % n
        else: return b
    raise ValueError(f'impossible! :(')

def rot_crypt(s:str, n:int, enc:bool = True) -> str:
    dn = n * (2 * enc - 1)
    x = ''
    for c in s.replace(' ','').lower():
        x += ALPHABET[(ALPHABET.index(c) + dn) % 26]
    if enc: x = x.upper()
    return x

