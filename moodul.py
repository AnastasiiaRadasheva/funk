def arithmetic(arv1: float, arv2: float, tehe: str)->any:
    """
    Lihne kalkulaator
    + - liitmine
    - - lahuntamine
    * - korrutamine
    / - jagamine
    ,
    :param float arn1: Sisend kasutajalt, mingi ujukomarv
    :param float arn2: Sisend kasutajalt, mingi ujukomarv
    :param str tehe: aritmeetiline tehe, mis valib kasutaja
    :rtype: var Määrata tüüp(float või str)
    """
    if tehe in ["+", "-", '*', '/']:
        if arv2==0 and tehe=='/':
            vastus = "DIV/0" # на ноль делить нельзя
        else:
            vastus = eval(str(arv1)+tehe+str(arv2))#eval соберет все и посчитает весь  пример
        return vastus


def is_year_leap(aasta: int)-> bool:
    """

    tagastab True, kui liigaasta ja
    false kui on tavalise aasta

    """
    if aasta%4==0:
        v = True
    else:
        v=False
    return v

def square(kulg:float)->any:
    '''
    ruut
    :param float kulg: Sisend kasutajalt, mingi arv
    arvutab ruudu umbermoot, pindala ja diagonaal
    :rtype: float tagastab umbermoot, pindala ja diagonaal
    '''
    umbermoot=kulg*4
    pindala=kulg**2
    diagonaal=(2)**(1/2)*kulg
    return umbermoot, pindala, diagonaal

def season(kuu:int)->str:
    '''
    aastaajad
    :param int kuu: Sisend kasutajalt, mingi arv
    tagastab aastaaja
    :rtype: str tagastab aastaaja
    '''
    if kuu in [12,1,2]:
        vastus="talv"
    elif kuu in [3,4,5]:
        vastus="kevad"
    elif kuu in [6,7,8]:
        vastus="suvi"
    elif kuu in [9,10,11]:
        vastus="sugis"
    return vastus

def bank(a: int, years: int)->int:
    '''
    : a int: sisend kui palju raha
    : years int : sisent mitu aastat
    '''
    vastus = a * (1+0.1*years)
    print(vastus)
    return vastus

def date (kuu:int, paev:int)->str:
    '''
    kuupaev
    :param int kuu: Sisend kasutajalt, mingi arv
    :param int paev: Sisend kasutajalt, mingi arv
    tagastab kuupaev
    :rtype: str tagastab kuupaev
    '''
    if kuu in [1,3,5,7,8,10,12]:
        if paev in range(1,32):
            vastus="kuupaev on oige"
        else:
            vastus="kuupaev on vale"
    elif kuu in [4,6,9,11]:
        if paev in range(1,31):
            vastus="kuupaev on oige"
        else:
            vastus="kuupaev on vale"
    elif kuu == 2:
        if paev in range(1,29):
            vastus="kuupaev on oige"
    else:
        vastus="kuupaev on vale"
    return vastus


def is_prime(arv: float) ->bool:
    """
    Kontrollib, kas number 
    tagastab True, kui liigaasta ja
    false kui on tavalise 
    rtype: bool

    """

def is_prime(arv):
    if arv < 2 or arv > 1000:
        return False
    for i in range(2, n):
        if arv % i == 0:
            return False
    return True


# def XOR_cipher(str: str, key:str) ->str: 