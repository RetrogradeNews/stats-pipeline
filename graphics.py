from PIL import Image, ImageDraw, ImageFont
import os

# Creates stats summary image for each author
def createGraphic(author, numPieces, mostViews, totalViews):
    # Creates a new image
    img = Image.new('RGB', (800, 1400), color='white')

    # Initializes image and fonts
    draw = ImageDraw.Draw(img)
    h1 = ImageFont.truetype(os.path.join("fonts", "CormorantGaramond-VariableFont_wght.ttf"), 60)
    h2 = ImageFont.truetype(os.path.join("fonts", "CormorantGaramond-VariableFont_wght.ttf"), 50)

    # Draws text
    draw.text((center(author, h1, img, draw),200), author, fill='black', font=h1)
    
    draw.text((center("Total Works Published", h2, img, draw),400), "Total Works Published", fill='purple', font=h2)
    draw.text((center(str(numPieces), h2, img, draw),460), str(numPieces), fill='blue', font=h2)

    draw.text((center("Total Views", h2, img, draw),570), "Total Views", fill='purple', font=h2)
    draw.text((center(str(totalViews), h2, img, draw),630), str(totalViews), fill='blue', font=h2)

    draw.text((center("Most Viewed Work", h2, img, draw),740), "Most Viewed Work", fill='purple', font=h2)
    draw.text((center(mostViews, h2, img, draw),800), mostViews, fill='blue', font=h2)

    # Saves the image as a PNG
    img.save(os.path.join("graphics", f"{author.replace(" ","")}Stats.png"))

# Calculates centered text location x
def center(text, font, img, draw):
    # Adds text
    bbox = draw.textbbox((0, 0), text, font=font)

    # Calculate text width and height
    text_width = bbox[2] - bbox[0]

    # Get image size
    image_width = img.size[0]

    # Calculate top-left coordinates to center the text
    x = (image_width - text_width) // 2
    return x