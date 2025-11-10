# Block 3: Villkorssatser (20 övningar)
# Instruktion: Nu introducerar vi if, elif, else och typkonvertering (int(), float()).




# 6.  Fråga användaren "Svara Ja eller Nej". Om svaret, oavsett versaler, är "ja", skriv ut "Du valde att fortsätta äventyret!".
# 7.  Fråga efter en spelares status (t.ex. "redo" eller "upptagen"). Om status inte är "redo", skriv "Vänta... Spelaren är inte redo.".
# 8.  Fråga hur många guldmynt du har (som ett tal). Om du har färre än 50, skriv ut "Du har inte råd med det här svärdet.".
# 9.  Fråga efter din karaktärs level (som ett tal). Om din level är 10 eller högre, skriv "Du kan lära dig formeln 'Fireball'!".
# 10. Fråga efter ålder (som tal) och om de har en biljett (som text, "ja" eller "nej"). Om personen är över 17 OCH har en biljett ("ja"), skriv "Välkommen in på konserten!".
# 11. Fråga om du har en "Guldnyckel" (ja/nej) eller en "Dyrk" (ja/nej). Om du har nyckel ("ja") ELLER dyrk ("ja"), skriv "Du lyckas öppna kistan!".
# 12. Skapa en variabel är_förbannad = True. Om karaktären inte är förbannad, skriv "Dina attacker gör normal skada.". Annars, skriv "Dina attacker är svagare!".
# 13. Fråga användaren efter deras namn. Om de skrev in ett namn (dvs. strängen inte är tom), skriv ut "Hej, [namn]!".
# 14. Fråga användaren efter deras namn. Om de inte skrev in något (dvs. strängen är tom), skriv ut "Du måste ange ett namn för att spara spelet!".
# 15. Fråga hur många liv användaren har (som ett tal). Om antalet liv är 0, skriv ut "Game Over".
# 16. Skapa förbjudna_föremål = "kniv bomb". Fråga vad användaren har i väskan. Om "bomb" finns i svaret, skriv "Säkerhetskontroll! Du stoppas!".
# 17. Fråga användaren om ett postnummer (som text). Kontrollera om inmatningen endast består av siffror. Om ja, skriv "Giltigt format.".
# 18. Fråga användaren om deras förnamn (som text). Kontrollera om inmatningen endast består av bokstäver. Om den inte gör det, skriv "Ett namn får inte innehålla siffror eller symboler.".
# 19. Fråga efter ett lösenord (som text). Om lösenordet är kortare än 8 tecken, skriv "Lösenordet är för kort! Minst 8 tecken krävs.".
# 20. Fråga "Vad väljer du? (attack/försvar/magi)".
# • Om valet är "attack", skriv "Du svingar ditt svärd!".
# • Om valet är "försvar", skriv "Du höjer din sköld!".
# • Om valet är "magi", skriv "Du kastar en formel!".
# • Annars, skriv "Ogiltigt val."

# 1.  Fråga användaren "Hur många bananer har du?". Konvertera svaret till ett heltal och spara i en variabel.
# while True:
#     try:
#         svar = int(input("Hur många bananer har du? "))
#         print(f"Du har {svar} bananer")
#         break
#     except ValueError:
#         print("Skriv ett heltal")

# while True:
#     try:
#         name = str(input("Enter your name: "))
#         if name.isalpha():
#             print(f"Your name is: {name.capitalize()}")
#             break
#         else:
#             print("Only enter valid text")
#     except ValueError:
#         print("Please enter only text")

# 2.  Fråga användaren "Vad är priset på en Potion? (t.ex. 19.5)". Konvertera svaret till ett flyttal.
# while True:
#     try:
#         pris = float(input("Vad är priset på en Potion? "))
#         print(f"Pris för en potion är: {pris:.2f}")
#         break
#     except ValueError:
#         print ("Enter only number")
# 3.  Fråga efter användarens ålder (som ett tal). Om åldern är 18 eller mer, skriv ut "Tillträde beviljas.".
# while True:
#     try:
#         age = int(input("What is your age: "))
#         if age >=18:
#             print("Tillträde beviljas.")
#             break
#         else:
#             print("You are not allowed to enter")
#             break
#     except ValueError:
#         print("Enter only digit")
# 4.  Fråga efter det magiska ordet. Om ordet är exakt "DevOps", skriv ut "Porten öppnas!". Annars, skriv ut "Fel ord! Porten förblir stängd.".
# while True:
#     try:
#         ordet = input("Give magiska ord: ")
#         if ordet.isalpha() and ordet == "DevOps":
#             print("Porten öppnas!")
#             break
#         else:
#             print("Fel ord! Porten förblir stängd.")
#     except ValueError:
#        print("Only Text")
# 5.  Fråga efter temperaturen ute (som ett tal).
# • Om den är över 25: Skriv ut "Det är sommarvarmt!".
# • Om den istället är över 15: Skriv ut "Det är lagom svenskt väder.".
# • Annars: Skriv ut "Det är kallt, ta på jackan!".
while True:
    try:
        temrature = int(input("What is temrature outside: "))
        if temrature>25:
            print("Det är sommarvarmt!")
            break
        elif temrature >15:
            print("Det är lagom svenskt väder.")
            break
        else:
            print("Det är kallt, ta på jackan!")
            break
            
    except ValueError:
        print("Enter only digit")




                  
