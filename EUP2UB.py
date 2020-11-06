# file handling
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "wardrobe.ini"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

#vars
wardrobeName = ""
wardrobeDict = dict()
allWardrobes = dict()

# xref of input keys to output keys
xref = dict()
xref = {
"Hat": ("prop_hats", "tex_hats"),
"Glasses": ("prop_glasses", "tex_glasses"),
"Ear": ("prop_ears", "tex_ears"),
"Watch": ("prop_watches", "tex_watches"),
"Top": ("comp_shirtoverlay", "tex_shirtoverlay"),
"UpperSkin": ("comp_shirt", "tex_shirt"),
"Decal": ("comp_decals", "tex_decals"),
"UnderCoat": ("comp_accessories", "tex_accessories"),
"Pants": ("comp_pants", "tex_pants"),
"Shoes": ("comp_shoes", "tex_shoes"),
"Accessories": ("comp_eyes", "tex_eyes"),
"Armor": ("comp_tasks", "tex_tasks")
}

# consume wardrobe.ini
for line in fhand:
    line = line.rstrip()
    if line.startswith("[") : #find start of individual wardrobe and save/print name
        wardrobeName = line.strip('[]')
        wardrobeDict = dict() #clear wardrobe on new wardrobe. otherwise wardrobes get overwritten
        #print(wardrobeName)
    
    if not line.startswith("[") : #for each comp, process into dict
        compValues = line.split("=")
        #print(compValues)
        if compValues[0] in xref :
            #print(compValues[1])
            numbersList = compValues[1].split(":")
            wardrobeDict[compValues[0]] = (numbersList[0], numbersList[1])
            #print(numbersList)
            #print(wardrobeDict)
    
            allWardrobes[wardrobeName] = wardrobeDict

# print(xref, "\n\n")
# print(allWardrobes, "\n\n")

#use dict.get to pull xref and create output 


for wardrobe in allWardrobes :
    print(wardrobe)
    #print(allWardrobes[wardrobe])
    output = "<Ped"
    for comp in allWardrobes[wardrobe] :
        compName = str(xref.get(comp)[0])
        compValue = int(allWardrobes[wardrobe][comp][0])
        textureName = str(xref.get(comp)[1])

        textureValue = int(allWardrobes[wardrobe][comp][1])

        if compValue > 1 or textureValue > 1 : #if the comp is not default or has a nondefault texture : print comp
            output += " {0}=\"{1}\"".format(compName, compValue)
            if textureValue > 1 : #if texture is not default : print texture
                output += " {0}=\"{1}\"".format(textureName, textureValue)

        #print(allWardrobes[wardrobe][comp])
    output += ">INSERT PED NAME HERE</Ped>"
    print(output, "\n")

    #### add feature to insert ped name or default to MP_F_FREEMODE_01