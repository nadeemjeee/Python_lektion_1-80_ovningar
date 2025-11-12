# Block 4: Loopar (20 övningar)
# Instruktion: Nu introducerar vi for, while, range och break.

# 1.  En trollkarl kastar en formel 5 gånger. Använd en loop för att skriva ut "Abracadabra!" 5 gånger.
# for i in range(1,6):
#     print(f"{i}.Abracadabra!")

print()
# 2.  Spelet har 5 nivåer. Använd en loop för att skriva ut: "Startar nivå 1", "Startar nivå 2", ..., "Startar nivå 5".
# for i in range(1,6):
#     print(f"Startar nivå {i}")

# 3.  Skapa en variabel kod = "LÅST". Använd en loop för att skriva ut varje bokstav i koden på en ny rad.
# kod = "LÅST"
# for i in kod:
#     print(i)

# 4.  En fackla brinner. Skapa bränsle = 10. Använd en while-loop som kör så länge bränsle är större än 0. Inuti loopen, skriv ut bränsle och minska den sedan med 1.
# bränsle = 10
# while bränsle>0:
#     print(f"Bränsle {bränsle}")
#     bränsle-=1
# print("Facklan har slocknat!")

# 5.  En planta växer. Skapa höjd = 0. Använd en while-loop som kör så länge höjd är mindre än 5. Inuti loopen, skriv ut höjd och öka den sedan med 1.
    
# höjd = 0
# while höjd<5:
#     print(f"Höjd {höjd}")
#     höjd +=1
# print(f"Plantan slutade växa vid höjd {höjd}.")

# 6.  Du står framför en låst dörr. Skapa en evig loop. Inuti loopen, fråga "Vad är lösenordet?". Om svaret är "exit", avbryt loopen.

# while True:
#     answer = input("What is password: ")
#     if  answer.lower() == "exit":
#         print("Finished ...")
#         break
#     else:
#         print("wrong password. Try again ")
# 7.  En motor varvar upp. Använd en loop för att skriva ut alla jämna tal från 2 till 10 (dvs. 2, 4, 6, 8, 10).
# motor_varv=2
# while motor_varv<=10:
#     print(f"Motor varv {motor_varv}")
#     motor_varv+=2
# 8.  Loopa igenom alla tal från 1 till 10. Skriv bara ut de tal som är delbara med 3.
# for i in range (1,11):
#     if i%3==0:
#         print (i)
# 9.  Skapa magi = 20. Skriv en while-loop som kör så länge du har magi kvar. Inuti, fråga "Kasta formel? (ja/nej)". 
# Om "ja", minska magi med 5 och skriv ut "Du har [magi] kvar." Annars, avbryt loopen.
# magi = 20
# while magi <=20:
#     svar = input("Kasta formel? (ja/nej): ").lower()
#     if svar =="ja":
#         magi-=5
#         print(f"du har {magi} kvar")
#         if magi ==0:
#             print("Magi är slut")
#             break
        
#     else:
#         break
#Option 2
magi = 20
# while magi > 0:
#     svar = input("Kasta formel? (ja/nej): ").lower()
#     if svar == "ja":
#         magi -= 5
#         if magi > 0:
#             print(f"Du har {magi} magi kvar.")
#         else:
#             print("Magi är slut!")
#             break
#     else:
#         print("Du väljer att spara din magi.")
#         break
# 10. Fråga "Hur många gånger ska jag heja?". Konvertera svaret till ett tal och använd det i en loop för att skriva ut "Heja!" rätt antal gånger.

# svar = int(input("Hur många gånger ska jag heja? "))
# for i in range(1,svar+1):
#     print(f"Heja!{i}")
# 11. Ett säkert system kräver ett lösenord. Fråga efter ett lösenord. Så länge lösenordet är kortare än 6 tecken, skriv "För kort, försök igen!" och fråga på nytt.
# while True:
#     password = input("Give your password: ")
#     if len(password)<6:
#         print("Very short, try again")
#     else:
#         print("Your password is accepted") 
#         break
# 12. Skapa schema = "måndag tisdag onsdag". Dela upp strängen vid mellanslag och använd en loop för att skriva ut varje dag på en ny rad.
# schema = "måndag tisdag onsdag"
# days = schema.split()
# for d in days:
#     print(d)

# # or 
# schema = "måndag tisdag onsdag"
# days = schema.split()
# for i, d in enumerate (days, start=1):
#     print (f"{i}.{d}")

# 13. En bomb-timer räknar ner. Använd en loop för att skriva ut "5 4 3 2 1" (allt på samma rad, separerat av mellanslag).
# for i in range (5,0,-1):
#     print(i,end=" ")

# 14. Skapa en tom sträng svar = "". Så länge "ja" inte finns i svaret (oavsett versaler), fråga "Är du redo att starta spelet?".
# svar = ""
# while "ja" not in svar.lower():
#     svar = input("Är du redo att starta spelet? ")

# 15. Fråga användaren om ett ord. Loopa över varje bokstav. Om en bokstav är 'a', skriv "Hittade ett 'a'!".
# word = ""
# word = input("Give ur word: ")
# while "a" in word.lower():
#     print("Hittade ett 'a'!")
#     break
# # or 
# word = input("Ge ditt ord: ")
# for bokstav in word.lower():
#     if bokstav == "a":
#         print("Hittade ett 'a'!")

# 16. Skapa monster_besegrat = False. Skriv en while-loop som kör så länge monstret inte är besegrat. 
# Inuti, fråga "Attackera? (ja/nej)". Om "ja", skriv "Du vann!" och se till att loopen avslutas.
# monster_besegrat = False
# while not monster_besegrat:
#     attack = input("Attackera? (ja/nej) ").lower().strip()
#     if attack == "ja":
#         print("You win")
#         monster_besegrat=True

# 17. Du samlar poäng. Skapa total_poäng = 0. Loopa 5 gånger. Varje gång, lägg till 10 poäng till 
# total_poäng. Efter loopen, skriv ut den totala poängen.
# total_poäng = 0
# for i in range(1,6):
#     total_poäng +=10
# print(f"total poäng är:{total_poäng}")

# 18. Fråga "Ange ett positivt tal:". Så länge talet (konverterat till ett heltal) är mindre än 0 (dvs. negativt), fortsätt att fråga "Inte negativt! Försök igen:".
# tal = int(input("Ange ett positivt tal: "))
# while tal<0:
#     tal = int(input("Inte negativt! Försök igen:"))
# print("Bra jobbat")

# 19. Du har 3 våningar på ett hotell. Loopa 3 gånger. Inuti den loopen, ha en till loop som kör 2 gånger och skriver ut "Rum". Skriv ut "Våning" i den yttre loopen.
# for v in range (1,4):
#     print(f"Våning{v}")
#     for r in range(1,3):
#         print(f"Room{r}")

# 20. Skapa ett gissningsspel. Fråga "Gissa mitt favorittal (1-10):". Så länge svaret (som ett tal) inte är 7, skriv "Fel, gissa igen!". Om det är 7, skriv "Rätt!" och avbryt loopen.
# guess = int(input("Guess my number(1-10): "))
# while guess !=7:
#     guess = int (input("Fel, guess again!: "))
# print("Right")

# or
while True:
    try:
        guess = int(input("Guess my number(1-10): "))
        if guess !=7:
            print("Fel, guess again!")
        else:
            print("Bravo")
            break
    except ValueError:
        print("Only digits")






    