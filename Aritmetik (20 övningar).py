# Block 1: Aritmetik (20 övningar)
# Instruktion: I detta block ska du inte använda input(). Arbeta direkt med tal och variabler i koden.
# 
# 
# 
# 
# 
# 
# 
# 8.  Om 25 bönor delas mellan 7 trollkarlar, hur många bönor blir över till dig? Skriv ut antalet.
# 9.  En magisk attack gör 3 upphöjt till 4 i skada. Beräkna och skriv ut hur mycket skada den gör.
# 10. Ett monster tappar 10 guld och 2 andra fiender tappar 5 guld var. Vad blir 10 + 2  5? Skriv ut resultatet.
# 11. Två lag, ett med 10 och ett med 2 spelare, får 5 poäng var. Vad blir (10 + 2)  5? Skriv ut resultatet.
# 12. Du packar din väska. Använd en print()-sats för att skriva ut "Fackla", "Rep" och "Svärd", separerade av ---.
# 13. Skriv ut en laddningssekvens. Använd två print()-satser för att skriva ut "Analyserar data..." och "Klar!" på samma rad.
# 14. Din karaktärs magi-poäng (mana) är 80.5. Spara detta i en variabel mana och skriv ut den.
# 15. Din mana är 80.5. Du kastar en formel som kostar 15.5. Beräkna och skriv ut hur mycket mana du har kvar.
# 16. Skapa del1 = "Cyber" och del2 = "Punk". Skapa och skriv ut en ny sträng som sätter ihop dem till ett ord.
# 17. Skapa strängen varningsljud = "Pip! ". Skapa och skriv ut en ny sträng där varningsljudet upprepas 5 gånger.
# 18. 160 rymd-marinsoldater ska sova i kapslar som rymmer 7 personer var. Skriv ett program som skriver ut:
# 1.  Antal fulla kapslar.
# 2.  Antal soldater som blir över.
# 19. Ett rymdskepp kostar 5000.0 krediter. Beräkna och skriv ut priset efter en prisökning på 10% (dvs. multiplicera med 1.10).
# 20. Använd en print()-sats för att rapportera din status: "Level:", 5, "och HP:", 100.

#1.  Skriv ett program som skriver ut texten "Välkommen, krigare!".
text = "Välkommen, krigare!"
print(f"{text}")

#2.  Din karaktär har 100 HP (Health Points). Spara detta i en variabel hp och skriv ut den.
hp = 100
print(f"Din karakt är har {hp} HP")

#3.  Du har 50 guldmynt. Du hittar en kista med 125 mynt. Beräkna och skriv ut din nya totala förmögenhet.
guldmynt = 50
nya_mynt = 125
total_mynter = guldmynt+nya_mynt
print(f"Du har total {total_mynter} mynter")

#4.  Ett rymdskepp har 500 i sköld-energi. En laserstråle träffar och gör 120 i skada. Beräkna och skriv ut energin som är kvar.
rymdskepp_energi = 500
forlorade_energi = 401
kvar_energi = rymdskepp_energi-forlorade_energi
print(f"Kvar energi är {kvar_energi}")
if kvar_energi<100:
    print("Energi är nästan slut")
else:
    print("Energi är stabilt")

# 5. Du köper 4 "health potions". Varje potion kostar 30 guld. Beräkna och skriv ut den totala kostnaden.
health_potions = 4
pris_potions = 30
total_pris = health_potions*pris_potions
print(f"Total pris är {total_pris} guld")

#6. En skatt på 150.0 guldmynt ska delas exakt lika mellan 2 pirater. Hur mycket får var och en? Skriv ut resultatet.
guld_mynt = 150.0
antal_pirater = 2
guld_mynt_pirater = (guld_mynt/antal_pirater)
print(f"Varje Pirat får : {guld_mynt_pirater:.2f} guldmynt")

#7.  25 magiska bönor ska delas lika mellan 7 trollkarlar. Hur många hela bönor får varje trollkarl? Skriv ut antalet.