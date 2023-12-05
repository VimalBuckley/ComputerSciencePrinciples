from PIL import Image

earth = Image.open("CS13_Earth.png")
dog = Image.open("CS13_GoldenRetriever.jpg")
smaller_earth = earth.resize((30, 30))
dog.paste(smaller_earth, (60, 50), mask=smaller_earth)
dog.paste(smaller_earth, (120, 55), mask=smaller_earth)
dog.show()