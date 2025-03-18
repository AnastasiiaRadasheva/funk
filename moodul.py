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

def square()