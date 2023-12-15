from PIL import Image, ImageDraw, ImageChops
import math

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

# def main(size: tuple, images: list):
#     angle = math.pi * 2 / len(images)
#     print(math.degrees(angle))
#     mask = Image.new("RGBA", size, (0,0,0,0))
#     drawable = ImageDraw.Draw(mask)
#     drawable.polygon(
#         [
#             (size[0] / 2, size[1] / 2),
#             (size[0], size[1] / 2),
#             (size[0], size[1] / 2 - size[0] / 2 * math.tan(angle))
#         ],
#         "red"
#     )
#     for i in range(7):
#         rotated = mask.rotate(45 + 45 * i)
#         mask.paste(rotated, mask=rotated)
    
#     roundImage(mask, 0.5).show()
    
def main(radius: int, images:list):
    angle = 2 * math.pi / len(images)
    empty = Image.new("RGBA", (radius, radius), (0, 0, 0, 0))
    mask = Image.new("RGBA", (radius, radius), (0, 0, 0, 0))
    drawableMask = ImageDraw.Draw(mask)
    drawableMask.polygon(
        [
            (radius / 2, radius / 2),
            (radius, radius / 2),
            (radius, radius / 2 * (1 - math.tan(angle)))
            
        ],
        "red"
    )
    
    for i in range(len(images)):
        
    

if __name__ == "__main__":
    main((600, 600), [1, 1, 1, 1, 1, 1, 1, 1])