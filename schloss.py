# Die Funktion valid_inputs ist dazu da, Inputs zu validieren, die aus einer
# endlichen Liste stammen sollen, z.B. ["j","n"] für ja/nein oder ["a","b","c"] o.ä.
# Die Liste der validen Inputs wird als Parameter valid_inputs übergeben
# Die Funktion gibt den überprüften, validen Input aus.
def valid_input(valid_inputs = [],
        message = "Eingabe: ",
        invalid = "Kein gültiger Input. Versuche es erneut: ",
        value_err = "Hä?"):
    while True:
        try:
            x = input(message)
            if x in valid_inputs:
                return x
            else:
                print(invalid)
        except ValueError:
            print(value_err)

def eingang():
    print("Du stehst vor dem Eingang eines verlassenen Schlosses.")
    print("Gehst du hinein? (j/n)")
    if valid_input(["j","n"]) == "j":
        return "enter"
    else:
        return "leave"

def leave():
    print("Du drehst um und gehst nach Hause. Langweilig!")
    return "end"

def end():
    print("Ende.")

def enter():
    print("Du versucht, die Tür zu öffnen, aber du bist zu schwach.")
    print("Vielleicht solltest du mehr ins Gym gehen anstatt Python zu lernen.")
    return "end"

r = "eingang"

while True:
    if r == "eingang":
        r = eingang()
    elif r == "leave":
        r = leave()
    elif r == "enter":
        r = enter()
    elif r == "end":
        r = end()
        break