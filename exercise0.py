def cagr_berechnung(AK, EK, t):
    cagr = (EK / AK)**(1/t) -1
    return cagr

cagr_berechnung(100, 700, 30)
