import os, os.path
from CS14_RoundImage import roundImage
from PIL import Image
def main():
    try:
        os.mkdir("Pillow/RoundedPictures")
    except:
        pass

    for file in os.listdir("Pillow/Pictures"):
        try:
            image = Image.open("Pillow/Pictures/" + file)
            try:
                roundImage(image, 0.15).save("Pillow/RoundedPictures/Rounded" + file, "png")
            except:
                print("Error with saving " + file)
        except:
            print("Error with opening " + file)
        
if __name__ == "__main__":
    main()