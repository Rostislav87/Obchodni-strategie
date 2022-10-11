# Obchodní strategie na D1 grafu využívající indikátory Williams %R, Momentum a ATR

# Podmínky pro long pozici:
# Pokud je Williams %R s periodou 10 pod úrovni -90 a Momentum s periodou 25 je rostoucí

condition1 = int(input("Jaká je hodnota Williams %R(10):\n"))

if condition1 < -90:
    condition2 = input("Momentum je rostoucí nebo klesající?\n")
    if condition2 == "rostoucí":
        atr = float(input("Jaká je hodnota ATR(20)?\n"))
        atr = atr * 2
        print(f"Nastav long pozici a nastav Stop Loss o velikosti {atr} pipů.")    
    else:
        print("Žádný obchod.")
        
# Podmínky pro short pozici:
# Pokud je Williams %R s periodou 10 nad úrovni -10 a Momentum s periodou 25 je klesající

elif condition1 > -10:
    condition2 = input("Momentum je rostoucí nebo klesající?\n")
    if condition2 == "klesající":
        atr = float(input("Jaká je hodnota ATR(20)?\n"))
        atr = atr * 2
        print(f"Nastav short pozici a nastav Stop Loss o velikosti {atr} pipů.")  
    else:
        print("Žádný obchod.")
else:
    print("Žádný obchod.")


