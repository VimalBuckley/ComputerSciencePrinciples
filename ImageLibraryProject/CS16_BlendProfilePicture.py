from PIL import Image, ImageDraw
import math
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
  
def main(radius: int, images:list):
    angle = 2 * math.pi / len(images)
    mask = Image.new(mode="RGBA", size=(radius, radius), color=(0,0,0,0,))
    drawableMask = ImageDraw.Draw(mask)
    drawableMask.polygon(
        [
            (radius / 2, radius / 2),
            (radius, radius / 2),
            (radius, radius / 2 * (1 - math.tan(angle)))
            
        ],
        "red"
    )
    image = Image.new("RGBA", (radius, radius), (0,0,0,0))
    for i in range(len(images)):
        image.paste(images[i], mask=mask.rotate(math.degrees(angle) * i))
    rounded = roundImage(image, 0.5)
    os.chdir("..")
    rounded.show()
    rounded.save("ProfilePicture.png")
    
if __name__ == "__main__":
    os.chdir("ImageLibraryProject/Pictures To Profile")
    radius = 600
    images = []
    for image in os.listdir():
        images.append(Image.open(image).resize((radius, radius)))
    main(radius, images)