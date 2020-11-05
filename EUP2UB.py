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
"Watches": ("prop_watches", "tex_watches"),
"Top": ("comp_shirt", "tex_shirt")
}

# consume wardrobe.ini
for line in fhand:
    line = line.rstrip()
    if line.startswith("[") : #find start of individual wardrobe and save/print name
        wardrobeName = line.strip('[]')
        wardrobeDict = dict() #clear wardrobe on new wardrobe. otherwise wardrobes get overwritten
        #print(wardrobeName)
    
    if not line.startswith("[") : #for each prop, process into dict
        propValues = line.split("=")
        #print(propValues)
        if propValues[0] in xref :
            #print(propValues[1])
            numbersList = propValues[1].split(":")
            wardrobeDict[propValues[0]] = (numbersList[0], numbersList[1])
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
    for prop in allWardrobes[wardrobe] :
        propName = str(xref.get(prop)[0])
        propValue = int(allWardrobes[wardrobe][prop][0])
        textureName = str(xref.get(prop)[1])

        textureValue = int(allWardrobes[wardrobe][prop][1])

        if propValue > 1 or textureValue > 1 :
            output += " {0}=\"{1}\" {2}=\"{3}\"".format(propName, propValue, textureName, textureValue)

        #print(allWardrobes[wardrobe][prop])
    output += ">INSERT PED NAME HERE</Ped>"
    print(output)

