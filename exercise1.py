def cagr_berechnung(AK, EK, t):
    cagr = ((EK / AK)**(1/t) -1)
    return cagr

cagr = cagr_berechnung(100, 700, 30) * 100

AK = 120
t = 30 
cagr = cagr_berechnung(100, 700, 30)
EK = AK * (1 + cagr)**t

print(EK)
