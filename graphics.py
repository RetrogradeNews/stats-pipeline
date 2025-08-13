from datetime import date
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

# Creates stats summary image for each author
def createGraphic(author, numPieces, mostViews, totalViews):

    # Color palette (i do not care that some of these colors may be predefined)
    RGbg = "#0C0C0F"    # Background color. Probably going to be close to black
    RGp1 = "#583192"    # This is the first official RG purple
    RGp2 = "#8953A1"    # This is the second offical RG purple
    RGb = "#4991CE"     # This is the offical RG blue
    RGc = "#8AF3FF"     # This cyan isn't part of the offical lineup. However. Pretty
    RGm = "#BE1589"     # An RG magenta. Only used in pie chart.
    RGp = "#FF8AA1"     # An RG pink. Only used in pie chart


    # Width and height variables
    width  = 1250
    height = 2000
    buffer = 20

    #bgColor = [29, 70, 95] # = #1D075F
    #bgColor = [247, 200, 218]
    # Creates a new image
    #img = Image.new('RGB', (width, height), color=f"rgb({bgColor[0]}, {bgColor[1]}, {bgColor[2]})")
    img = Image.new('RGB', (width, height), color=RGbg)

    # Font height for the "top stories"
    h3h = 40

    # Initializes image and fonts. Added Inter Tight
    draw = ImageDraw.Draw(img)
    h1 = ImageFont.truetype(os.path.join("fonts", "CormorantGaramond-VariableFont_wght.ttf"), 100)
    h2 = ImageFont.truetype(os.path.join("fonts", "CormorantGaramond-VariableFont_wght.ttf"), 50)
    h3 = ImageFont.truetype(os.path.join("fonts", "InterTight-VariableFont_wght.ttf"), h3h)
    h4 = ImageFont.truetype(os.path.join("fonts", "CormorantGaramond-VariableFont_wght.ttf"), h3h)

    ##########################################
    # BACKGROUND DETAILS
    # Right top
    # line circles
    draw.circle((1200, 200), 125, fill=None, outline=RGc, width=5)
    draw.circle((1150, 400), 225, fill=None, outline=RGb, width=5)
    # clear
    draw.circle((1200, 200), 120, fill=RGbg, outline=None, width=0)
    draw.circle((1150, 400), 220, fill=RGbg, outline=None, width=0)
    # body circles
    draw.circle((1200, 200), 100, fill=RGp2, outline=None, width=0)
    draw.circle((1150, 400), 200, fill=RGp1, outline=None, width=0)
    # Top
    draw.circle((850, -275), 400, fill=RGb,  outline=None, width=0)
    draw.circle((850, -275), 420, fill=None, outline=RGp2, width=5)
    draw.circle((850, -275), 440, fill=None, outline=RGp1, width=5)
    # Left side
    draw.circle((-25,  1100), 235, fill=RGp1, outline=None, width=0)
    draw.circle((-25,  1100), 255, fill=None, outline=RGb,  width=5)
    draw.circle((-25,  1100), 275, fill=None, outline=RGc,  width=5)
    # Dot color samples
    dot = 45
    doh = 240 # Dot height [-75]
    draw.circle((dot, doh+1*75),  25, fill=RGp1, outline=None,  width=0)
    draw.circle((dot, doh+2*75),  25, fill=RGp2, outline=None,  width=0)
    draw.circle((dot, doh+3*75),  25, fill=RGb,  outline=None,  width=0)
    draw.circle((dot, doh+4*75),  25, fill=RGc,  outline=None,  width=0)
    draw.circle((dot, doh+5*75),  25, fill=RGb,  outline=None,  width=0)
    draw.circle((dot, doh+6*75),  25, fill=RGp2, outline=None,  width=0)
    draw.circle((dot, doh+7*75),  25, fill=RGp1, outline=None,  width=0)
    # Dot color samples pt 2
    dot = 1205
    doh = 600 # Dot height [-75]
    draw.circle((dot, doh+1*75),  25, fill=RGp1, outline=None,  width=0)
    draw.circle((dot, doh+2*75),  25, fill=RGp2, outline=None,  width=0)
    draw.circle((dot, doh+3*75),  25, fill=RGb,  outline=None,  width=0)
    draw.circle((dot, doh+4*75),  25, fill=RGc,  outline=None,  width=0)
    draw.circle((dot, doh+5*75),  25, fill=RGb,  outline=None,  width=0)
    draw.circle((dot, doh+6*75),  25, fill=RGp2, outline=None,  width=0)
    draw.circle((dot, doh+7*75),  25, fill=RGp1, outline=None,  width=0)
    # Almost in dots 2
    draw.circle((1140, 1245), 50, fill=RGp2, outline=None, width=0)
    draw.circle((1140, 1245), 70, fill=None, outline=RGc,  width=5)
    draw.circle((1140, 1245), 90, fill=None, outline=RGb,  width=5)
    # Top
    draw.circle((850, -275), 400, fill=RGb,  outline=None, width=0)
    draw.circle((850, -275), 420, fill=None, outline=RGp2, width=5)
    draw.circle((850, -275), 440, fill=None, outline=RGp1, width=5)   
    # Bottom
    draw.circle((1175, 2400), 800, fill=RGb,  outline=None, width=0)
    draw.circle((1175, 2400), 820, fill=None, outline=RGc,  width=5)
    draw.circle((1175, 2400), 840, fill=None, outline=RGp2, width=5) 
    draw.circle((1175, 2400), 860, fill=None, outline=RGp1, width=5) 
    # Bottom Left
    draw.circle((90, 1800), 100, fill=RGp2, outline=None, width=0)
    draw.circle((90, 1800), 120, fill=None, outline=RGp1, width=5)
    draw.circle((90, 1800), 140, fill=None, outline=RGb,  width=5) 

    ##########################################
    # NAME HEADING
    head = 110  # size, related to font size
    offhX = 25  # padding (off) for the (h)eader in the (X) direction
    offhY = 50  # padding (off) for the (h)eader in the (Y) direction
    draw.circle((head+offhX, head+offhY), head, fill=RGb, outline=None, width=0)        # Circle for half circle
    draw.rounded_rectangle([(head+offhX, offhY), (3*head+offhX, 2*head+offhY)], radius=0, fill=RGbg, corners=(True,True,True,True))      # Half for half circle (this could've been an arc)
    draw.arc([(offhX, offhY-25), (offhX+2*head, 2*head+offhY-25)], 91, 271, fill=RGc, width=5)
    draw.circle((offhX+head,2*head+offhY-28), 10, fill=RGc, outline=None, width=0)           # Dot
    # Name: assumes first names are always just one word. Surnames can be as many names as they want
    firstName = author.split()[0]
    surelyThereWasABetterWayToDoThis = author.split()[1:]
    lastName = ""
    for x in surelyThereWasABetterWayToDoThis:
        lastName = lastName + x + " "
    # draw.text((x, y), text, fill=None, font=None, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False, font_size=None)
    draw.text((head+offhX+buffer, offhY-10), firstName, fill="white", font = h1)      # First name
    draw.text((head+offhX+buffer, offhY+head-10), lastName, fill="white", font = h1)  # Last name
    draw.line([(head+offhX,offhY-23), (head+offhX+rightBox(firstName, h1, draw),offhY-23)], fill=RGc, width=5, joint=None)      # Overline
    draw.circle((head+offhX+rightBox(firstName, h1, draw),offhY-23), 10, fill=RGc, outline=None, width=0)                       # Dot on overline

    ##########################################
    # TOTAL WORKS AND VIEWS
    offtX = 90                      # padding (off) for the (t)otal works and views in the (X) direction
    offtY = offhY + 2*head + buffer # padding (off) for the (t)otal works and views in the (Y) direction
    boxth = 120                     # (h)eight of the (box)es in the (t)otal works and views area
    twp = "Total Works Published"
    tv  = "Total Views"
    tRatio = 2/3
    tvBoxSize = (width - 2*offtX - buffer)*(1-tRatio)
    twpBoxSize = (width - 2*offtX - buffer)*tRatio
    twpBoxOffset = centerBox(twp, h2, twpBoxSize, draw)
    twpNumOffset = centerBox(str(numPieces), h3, twpBoxSize, draw)
    tvBoxOffset = centerBox(tv, h2, tvBoxSize, draw)
    tvNumOffset = centerBox(str(totalViews), h2, tvBoxSize, draw)
    offsettvX = offtX + twpBoxSize + buffer
    # "Total works published" box
    draw.rounded_rectangle([(offtX, offtY-10), (offtX+twpBoxSize, offtY+boxth)], radius=buffer, fill=RGbg, outline=RGb, width=5, corners=(True,True,True,True))
    draw.text((offtX + twpBoxOffset, offtY), twp, fill="white", font=h2)
    draw.text((offtX + twpNumOffset, offtY + 60), str(numPieces), fill=RGb, font=h3)
    # "Total views" box
    draw.rounded_rectangle([(offsettvX, offtY-10), (offsettvX+tvBoxSize, offtY+boxth)], radius=buffer, fill=RGbg, outline=RGb, width=5, corners=(True,True,True,True))
    draw.text((offsettvX+tvBoxOffset, offtY), tv, fill="white", font=h2)
    draw.text((offsettvX+tvNumOffset, offtY + 60), str(totalViews), fill=RGb, font=h3)

    
    ##########################################
    # TOP 3
    # TODO: Make this legitimate. 
    # Format: topThree is an array with tuples of (story name, view count)
    offt3X = 120 
    offt3Y = offtY + boxth + buffer + 10
    boxt3h = 800                     # (h)eight of the (box) in the (t)op (3) area
    # Box for the Top 3                                                                 
    draw.rounded_rectangle([(offt3X-buffer-10, offt3Y-10), (width-(offt3X-buffer-10), offt3Y + boxt3h)], radius=100, fill=RGbg, outline=RGb, width=5, corners=(True,True,True,True))
    titleRoom = 800
    t3 = "Top 3 Works:"
    topThree = [(mostViews, 1000), ("Second story here Second story here Second story here Second story here Second story here", 800), 
               ("This is a third story and the hope is this triggers a line break yeeeeehawwwww",690)]
               #("Four through eleven", 411), ("Number 15: Burger king foot lettuce", 15)]
    # Top 3 title text
    draw.text((center(t3, h1, img, draw), offt3Y), t3, fill='white', font=h1) 
                # h3h is font height for h3, which is being used for the top 3 list
    line = 0    # Line number, starting at 0
    for i in range(0,len(topThree)):
        draw.text((offt3X, offt3Y+150+(h3h+20)*line), (str(i+1) + "."), fill=RGb, font=h3)  # The number
        draw.text((width - offt3X - 25 - rightBox(str(topThree[i][1]), h3, draw), 
                   offt3Y+150+(h3h+20)*line), str(topThree[i][1]), fill=RGb, font=h3)       # The view count
        lines = lineBreak(topThree[i][0], h3, titleRoom, draw)                              # Get the individual lines
        for x in lines:                                                                     # For each line:
            draw.text((offt3X + 50, offt3Y+150+(h3h+20)*line), x, fill='white', font=h3)    # print line
            line += 1
        line += 0.5   # Add a line to move to the text
    # draw.text((center(mostViews, h2, img, draw),800), mostViews, fill='blue', font=h2)

    ##########################################
    # CHART
    offcX = 25                              # padding (off) for the (c)hart in the (X) direction
    offcY = offt3Y + boxt3h + buffer + 10   # padding (off) for the (c)hart in the (Y) direction
    carth = 600                             # (c)h(art) (h)eight. Also an anagram of chart
    # So conceptualize two boxes. One has the Key, the other the Chart. Together there is width - 2 offcX space.
    # Pie chart should be pie should be circle should be height minus buffer.
    # Other side will then be box width minus 2 buffer minus pie
    pieR = carth/2 - buffer # (R)adius for the (pie) chart
    keyW = width - 2*offcX - 2*buffer - 2*pieR 
    # Box for the chart                                                                 
    draw.rounded_rectangle([(offcX, offcY-10), (width-offcX, offcY + carth)], radius=100, fill=RGbg, outline=RGb, width=5, corners=(True,True,True,True))
    BBS = "Breakdown by Section"            # CATEGORY
    #keyTitleoffset =  80                   # centerBox(BBS, h2, keyW, draw), with carth = 500. It looked good. It was 32 then I adjusted the box width
    draw.text((offcX + 125, offcY+10), BBS, fill='white', font=h2)
    #################
    # MUAAZ
    # THIS IS WHERE WE ADD CATEGORIES WITH KEYS. Sorted here, if not already sorted dw
    sectionsWithNums = [("Life & Arts", 1), ("Ed Desk", 10), ("News", 20),  
                        ("aaa", 2), ("bbb", 2), ("ccc", 2), ("ddd", 2),  
                        ("eee", 2), ("fff", 2), ("Comics & Activities", 2)]
    sections         = len(sectionsWithNums)
    sectionsWithNums = sorted(sectionsWithNums, key=lambda x: x[1], reverse=True)  
    # print(sectionsWithNums)
    # This is an array of colors. We can change them, but this is what we draw from for the pie chart
    # ... I've been in Newspaper, News, Breaking News, Opinion, LttE, Ed Desk, Editorial, C&A, L&A, and Sports. Fuck me 
    # For completeness we *could* get a total of 15 or so colors... which means we probably should. Here's 10 in the meantime.
    colors = [RGc, RGb, RGp2, RGp1, RGm, RGp, "#D69D85", "#D2E0AB", "#82ED87", "#37E6C0"]
    # So the center, vertically, is start height + (carth - 100)/2
    # And we adjust up by 25 automatically per total line
    # Morning me: this made sense to late night me
    centcY = offcY + 100 + (carth-100)/2    # the (cen)ter of (c)hart's key in the (Y) direction
    offccY = centcY - 25*sections           # the (off)set to the start relative to the (c)enter of (c)hart's key in the (Y) direction
    for i in range(sections):
        draw.circle((offcX +  79, offccY + 50*i), 20 , fill=colors[i], outline=None, width=0)
        draw.text(  (offcX + 129, offccY + 50*i - 25), sectionsWithNums[i][0], fill='white', font=h3)
    ########
    # THIS IS WHERE THE CHART PROPER GOES
    # box in which it fits:
    # draw.rectangle([(offcX + keyW, offcY + 10), (offcX + keyW + 2*pieR, offcY + 10 + 2*pieR)], fill='#0000FF80')
    # circle (for scale):
    draw.circle((offcX + keyW + pieR, offcY + 10 + pieR), pieR , fill='white', outline=None, width=0)
        
    ##########################################
    # BOTTOM TEXT
    offbtX = 25
    offbtY  = offcY + carth + buffer        # (Off)set for the (b)ottom (t)ext in the Y
    botth   = 85                            # (bot)tom (t)ext (height)
    draw.rounded_rectangle([(offbtX, offbtY), (width-offbtX, offbtY+botth)], radius=buffer, fill=RGbg, outline=RGp1, width=5, corners=(True,True,True,True))
    today = date.today()
    generatedDate = "Generated %s %s %s." %(today.year, today.strftime("%b"), today.strftime("%d"))
    ReportTitle = "Retrograde Report for AY 2024-2025. "
    bottomText = ReportTitle + generatedDate
    draw.text((center(bottomText, h2, img, draw), offbtY+10), bottomText, fill='white', font=h2)
    

    


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

# Takes in a width and text, returns offset from left of box
def centerBox(text, font, box_width, draw):
    # Adds text, calculates width and height
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    # Calculate top-left coordinates to center the text
    x = (box_width - text_width) // 2
    return x

# Allows for optimization of right-aligned text (literally just gets text length)
def rightBox(text, font, draw):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    return text_width

# Goes through and assembles the lines for printing, returns array
# Assumes that there isn't a single word that exceeded the entire line width
def lineBreak(piece, font, box, draw):
    words = piece.split()
    arr = []
    while len(words) > 0:
        x = numValid(words, font, box, draw)
        if x == 0:
            return arr
        line = ""
        for a in words[0:x]: line = line + a + " "
        arr.append(line)
        words = words[x:]
    return arr                  # Possibly redundant but that's between the computer and God

# Gets the max (num)ber of words you can fit in a (valid) line
# Not my finest naming convention work
def numValid(words, font, box, draw):
    for i in range(len(words)):
        potLine = ""                                # Potential line
        for x in words[0:len(words)-i]:             # Actually creating the potential line
            potLine = potLine + x + " "     
        if rightBox(potLine, font, draw) < box:     # THIS IS CONDITIOJN
            # print(rightBox(potLine, font, draw))
            # print(box)
            return len(words)-i                     # Return the maximum length of words for the new line
    return -1
