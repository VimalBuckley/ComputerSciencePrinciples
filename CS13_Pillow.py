from PIL import Image, ImageChops, ImageDraw, ImageFont

background = Image.open("CS13_WhiteBackground.jpg")
font = ImageFont.truetype("CS13_OpenSans.ttf", 30)
drawable = ImageDraw.Draw(im=background)

drawable.text((100, 100), "- STOP DOING FUNCTIONAL PROGRAMMING", font=font, fill="red")
drawable.text((100, 150), "- Code is not meant to function", font=font, fill="red")
drawable.text((100, 200), "- Years of coding, yet NO REAL-WORLD USE FOUND \n   for not using OOP", font=font, fill="red")
drawable.text((100, 300), "- Wanted to write efficent code? We had a tool for that:\n   It was called ASSEMBLY", font=font, fill="red")
drawable.text(
    (100, 400), 
    "- 'Yes, please give me a CLOSURE of something. Please give me\n   a MONAD of it' - Statements dreamed up by evil wizards", 
    font=font, 
    fill="red"
)
drawable.text(
    (100, 500),
    "- LOOK at what FUNCTIONAL PROGRAMMERS have been demanding your Respect" + 
    "\n  for all this time, with all the LANGUAGES and COMPILERS we built for them",
    font=font,
    fill="red"
)

background.show()
