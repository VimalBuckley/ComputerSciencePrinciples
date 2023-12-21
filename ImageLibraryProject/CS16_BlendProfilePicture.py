from PIL import Image, ImageDraw
import math
import os, os.path

def roundImage(imageToMask: Image, borderPercent: float): # The round image method from before
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
    os.chdir("ImageLibraryProject/Pictures To Profile") # Sets the current directory to the "Picture To Profile" folder
    radius = 600 # Sets the radius of the profile picture
    images = [] # Create an empty list for images
    for image in os.listdir():
        images.append(Image.open(image).resize((radius, radius))) # Add all the files from the folder to the images list
    angle = 2 * math.pi / len(images) # Calculate the angle for each image based on the number of images
    mask = Image.new(mode="RGBA", size=(radius, radius), color=(0,0,0,0,)) # Create an image to be a mask. Make sure it's invisible
    drawableMask = ImageDraw.Draw(mask) # Create a drawable version of the mask
    drawableMask.polygon( # Draw a triangle based on the angle calculated before
        [
            (radius / 2, radius / 2),
            (radius, radius / 2),
            (radius, radius / 2 * (1 - math.tan(angle)))
        ],
        "red"
    )
    image = Image.new("RGBA", (radius, radius), (0,0,0,0)) # Make an image to paste stuff on
    for i in range(len(images)):
        image.paste(images[i], mask=mask.rotate(math.degrees(angle) * i)) # Paste all the images on our image
    rounded = roundImage(image, 0.5) # Round our image
    os.chdir("..") # Set our directory back to the overall folder
    rounded.show() # Show the new image
    rounded.save("ProfilePicture.png") # Save it
    
if __name__ == "__main__": # Making sure this only runs when its run directly, and not if it's imported
    main()