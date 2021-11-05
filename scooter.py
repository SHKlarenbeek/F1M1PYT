print("hoeveel km rijd jij per maand op je scooter")

antwoord = input()

def bereken_maandkosten(km_per_maand):
    getal1 = verzekering_per_maand = 23
    getal2 = benzine_kosten_per_liter = 1.54
    getal3 = liter_per_kilometer = 0.2 
    getal4 = km_per_maand 
    maandkosten = getal1 + getal2 * getal3 * getal4

bereken_maandkosten()