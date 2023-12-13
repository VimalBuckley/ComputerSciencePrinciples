from PIL import Image, ImageDraw
import os, os.path

def roundImage(imageToMask: Image, borderPercent: float):
    mask = Image.new("RGBA", imageToMask.size, (0, 0, 0, 0))
    borderPercent = abs(borderPercent)
    if borderPercent > 0.5:
        borderPercent = 0.5
    width, height = mask.size
    drawable = ImageDraw.Draw(mask)
    widthOffset = width * borderPercent
    heightOffset = height * borderPercent
    drawable.rectangle([(widthOffset, 0), (width - widthOffset, height)], fill="blue")
    drawable.rectangle([(0, heightOffset), (width, height - heightOffset)], fill="blue")
    drawable.ellipse([(0, 0), (2 * widthOffset, 2 * heightOffset)], fill="blue")
    drawable.ellipse([(width - 2 * widthOffset, 0), (width, 2 * heightOffset)], fill="blue")
    drawable.ellipse([(0, height - 2 * heightOffset), (2 * widthOffset, height)], fill="blue")
    drawable.ellipse([(width - 2 * widthOffset, height - 2 * heightOffset), (width, height)], fill="blue")
    final = Image.new(mode = "RGBA", size=imageToMask.size, color=(0, 0, 0 ,0))
    final.paste(imageToMask, (0, 0), mask)
    return final

def main():
    # print(os.listdir())
    for file in os.listdir("Pillow/Pictures"):
        roundImage(Image.open("Pillow/Pictures/"+file), 0.25).show()    

if __name__ == '__main__':
    main()


