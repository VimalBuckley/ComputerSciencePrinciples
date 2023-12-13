from PIL import Image, ImageChops, ImageDraw, ImageFont

background = Image.open("Pillow/Pictures/CS13_WhiteBackground.jpg")
font = ImageFont.truetype("Pillow/Fonts/CS13_OpenSans.ttf", 30)
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
drawable.text(
    (300, 600),
    "This is real CODE, written by REAL CODERS",
    font=font,
    fill="red"
)

pic1 = Image.open("Pillow/Pictures/CS13_FuncProg1.png").resize((350, 150))
pic2 = Image.open("Pillow/Pictures/CS13_FuncProg2.png").resize((450, 150))
pic3 = Image.open("Pillow/Pictures/CS13_FuncProg3.jfif").resize((400, 150))

background.paste(pic1, (50, 650))
background.paste(pic2, (400, 650))
background.paste(pic3, (850, 650))

drawable.text(
    (200, 800),
    "??????                                       ???                                                   ????",
    font=font,
    fill="red"
)
drawable.text(
    (350, 850),
    "Hello, I would like SETOID apples please",
    font=font,
    fill="red"
)
drawable.text(
    (360, 900),
    "They have played us for absolute fools",
    font=font,
    fill="red"
)
background.show(title="Custom Meme")