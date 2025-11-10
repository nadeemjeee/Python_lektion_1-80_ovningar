# Instruktion: I detta block får du använda input() för att hämta text. Du ska inte konvertera text till siffror.

#1.  Fråga användaren "Vad är ditt agentnamn?" och spara svaret i en variabel agent_namn.
# agent_namn = input("What is your agent name: ")
#print(f"His name is {agent_namn.strip()}")

#2.  Fråga användaren efter deras hemplanet. Svara sedan "Trevligt! [planet] är en vacker plats."
# hemaplan = input("Which one is your home ground: ")
# print(f"Trevligt! {hemaplan.strip()} är en vacker plats.")

# # 3.  Skapa en variabel recept = "Pannkakor". Skriv ut den första bokstaven i receptnamnet.
# recept = "Pannkakor"
# print(recept[0])
# #4.  Använd samma recept-variabel. Skriv ut den sista bokstaven i receptnamnet.
# print(recept[-1])
# #5.  Skapa variabeln kodord = "DevOpsÄrKul". Skriv ut den första delen av ordet: "DevOps".
# kodord = "DevOpsÄrKul"
# print(kodord[0:6])
# # or
# print(kodord[:6])
# #6.  Använd samma kodord-variabel. Skriv ut den sista delen av ordet: "Kul".
# print(kodord[-3:])
# #7.  Skapa text = "abcRECEPTxyz". Skriv ut texten som finns mellan "abc" och "xyz".
# text = "abcRECEPTxyz"
# print(text[3:9])
# # or 
# print(text[3:-3])
# #8.  Använd kodord = "DevOpsÄrKul". Skriv ut hela ordet baklänges.
# print(kodord[::-1])
# #9.  Fråga användaren om ett hemligt lösenord. Skriv ut hur många tecken lösenordet har.
# losenord = str(input("Give your password: "))
# print(f"length of your password is {len(losenord)} alphabets")
#10. Skapa namn = "grogu". Skriv ut namnet med enbart STORA bokstäver.
# namn = "grogu"
# print(namn.upper())
#11. Fråga användaren "ATTACKERA ELLER FLY?". Spara svaret och skriv ut det med enbart små bokstäver.
# choice = str(input("ATTACKERA ELLER FLY: ").lower())
# print(choice)

# 12. Skapa en bok_titel = "sagan om ringen". Skriv ut den med stor första bokstav i varje ord (Title Case).
# bok_titel = "sagan om ringen"
# print(bok_titel.title())

# 13. En användare har matat in sitt namn med massa skräp: användarnamn = "  _anna_
# användarnamn = "  _anna_"
# print(användarnamn.strip(" _"))

# 14. Vi har ett felstavat meddelande: fel = "Jag gillar Jovo.". Ersätt "Jovo" med "Java" och skriv ut det rättade meddelandet.
# fel = "Jag gillar Jovo."
# print(fel.replace("Jovo", "Java"))
# 15. Du har en inköpslista som en enda sträng: lista = "mjölk,bröd,ägg". Dela upp strängen till en lista vid varje kommatecken och skriv ut listan.
# lista = "mjölk,bröd,ägg"
# new_lista = lista.split(",")
# print(new_lista)
# for i in new_lista:
#     print(i)

# 16. Skapa text = "Var i galaxen är Xur?". Ta reda på vilken position (index) "Xur" börjar på. Skriv ut positionen.
text = "Var i galaxen är Xur?"   
pos = text.find("Xur")
if pos !=-1:
    print(f"Oredet hittade på {pos}")
else:
    print("Ordet hittade inte")

# 17. Skapa ord = "banana". Räkna hur många gånger bokstaven 'a' förekommer. Skriv ut antalet.
ord = "banana"
print(ord.count("a"))

# 18. Skapa fil = "bild.jpg". Kontrollera om strängen börjar med "bild". Skriv ut True eller False.
fil = "bild.jpg"
print(fil.startswith("bild"))

# 19. Använd fil-variabeln från förra uppgiften. Kontrollera om den slutar med ".gif". Skriv ut True eller False.
print(fil.endswith("gif"))

# 20. Skapa mening = "lösenordet är: banan". Kontrollera om ordet "lösenordet" finns i meningen. Skriv ut True eller False.
mening = "lösenordet är: banan"
print("lösenordet" in mening)