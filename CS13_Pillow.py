from PIL import Image, ImageChops, ImageDraw

earth = Image.open("CS13_Earth.png")
dog = Image.open("CS13_GoldenRetriever.jpg")
smaller_earth = earth.resize((30, 30))
dog.paste(smaller_earth, (60, 50), mask=smaller_earth)
dog.paste(smaller_earth, (120, 55), mask=smaller_earth)
drawingDow = ImageDraw.Draw(dog)
drawingDow.text((50,200), "This is a dog!!", font_size=20)
dog.show()
