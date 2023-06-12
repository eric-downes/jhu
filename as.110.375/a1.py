from string import ascii_uppercase as ALPH
from collections import Counter
import re

NGramType = dict[frozenset[str], tuple[float, str]]

'classes'

class SubCipher:
    def __init__(self, ciphertext:str):
        self.engfreq = 'etaonrishdlfcmugypwbvkxjqz'
        self.ciphertext = re.sub('[^A-Z]','',ciphertext.upper())
        srtd = sorted(Counter(self.ciphertext).items(),
                      reverse = True, key = lambda x:x[1])
        self.byfreq = ''.join([v[0] for v in srtd])
    def state(self, a:str|dict[str,str] = {}, b:str = None):
        if not b: assert isinstance(a, dict)
        else: a = self.s2d(a, b)
        cipher = self.cipher | a
        s = ''
        for i, c in enumerate(self.ciphertext):
            if not i % 5: s += ' '
            if not i % 50: s += '\n'
            s += cipher.get(c, c)
        print(s)
    @staticmethod
    def s2d(a:str, b:str) -> dict[str,str]:
        if len(b) == 1: b *= len(a)
        assert len(a) <= len(b)
        return {frm.upper():to.lower() for frm, to in zip(a,b)}
    def fix(self, a:str, b:str, d:dict = {}):
        delta = d if d else self.s2d(a, b)
        self.cipher |= d
    def calc_ngrams(self, n:int):
        rng = range(len(self.ciphertext) - n)
        self.ngrams[n] = {k:v for k,v in sorted(
            Counter([ciphertext[i:i+n] for i in rng]),
            reverse = True, key = lambda x:x[1])}


'fcns'
    
def foreva(x):
    while True:
        yield x

def rot_crypt(s:str, n:int|Sequence[int], enc:bool = True) -> str:
    "'abcd' == rot_crypt(rot_crypt('abcd', 22), 22, False)"
    def dn(n:int): return n * (2 * enc - 1)
    s = re.sub('[^A-Z]', '', s.upper())
    if isinstance(n, int): n = foreva(n)
    x = [ALPH[(ALPH.index(c) + dn(ni)) % 26] for ni, c in zip(n, s)]
    return x.upper() if enc else x.lower()

def my_divmod(n:int, d:int):
    'my_divmod(n,d) == divmod(n,d) # just 2x slower :)'
    q = n // d
    return q, n - q * d

def gcd(i:int, j:int) -> int:
    sm, big = sorted((i, j))
    while sm: big, sm = (sm, big % sm)
    return big

def gcdx(i:int, j:int) -> tuple[int,int,int]:
    sm, big = sorted((i, j))
    u, up = 0, 1
    vp, v = 0, 1
    while sm:
        q, r = divmod(big, sm)
        big, sm = (sm, r)
        up, u = (u, up - q * u)
        vp, v = (v, vp - q * v)
    return (big, up, vp)

def ord_p(n:int, p:int) -> int:
    '(gcd(y,x) == 1) iff (ord_p(x**k * y, x) == k)'
    assert p > 0
    if p == 1: return 0
    for k in range(n):
        n, r = divmod(n, p)
        if r: break
    return k

def pow_sqmul(a:int, x:int, n:int) -> int:
    'pow_sqmul(a,x,n) == pow(a,x,n) == a**x % n'
    assert a > 0 and x > 0 and n > 0
    b = 1
    while True:
        x, r = divmod(x, 2)
        if r: b = b * a % n
        if a == 1 or not x:
            return b
        a = a * a % n
        

