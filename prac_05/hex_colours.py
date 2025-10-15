"""
CP1404/CP5632 Practical
Colour names in a dictionary
"""

COLOUR_NAME_HEX = {
    "Pink Flamingo": "#FC74FD",
    "Acid Green": "#B0BF1A",
    "AliceBlue": "#F0F8FF",
    "Kombu Green": "#354230",
    "Amaranth": "#E52B50",
    "Granny Smith Apple": "#A8E4A0",
    "Lapis Lazuli": "#26619C",
    "Light French Beige": "#C8AD7F",
    "Orange Soda": "#FA5B3D",
    "Persian Pink": "#F77FBE"
}

colour_code = input("Enter A Colour Name For A Hex: ")
while colour_code != "":
    if colour_code in COLOUR_NAME_HEX:
        print(colour_code, "is", COLOUR_NAME_HEX[colour_code])
    else:
        print("Invalid Colour Code")
    colour_code = input("Enter A Colour Name For A Hex: ")


