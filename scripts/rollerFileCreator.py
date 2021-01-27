# rollerskatespots new spot file creator

# todo: spotTemplate.html doesn't exist apparently in the same directory

##########

import codecs # for opening html files
import os # for checking if file exists

def skatespot():
    print("Creating new skatespot...")
    
    # read template file
    readTemplate = codecs.open("scripts/spotTemplate.html", "r")
    print(readTemplate.read())
    
    # create new file
    fileName = locationName.replace(" ", "")

    # if file already exists, delete and create a new file
    if os.path.exists(fileName+".html"):
        os.remove(fileName+".html")
    newFile = open(fileName+".html", "x") 
    
    # write template text to file
    # newFile.write(str(readTemplate))
    fillTemplate = str(readTemplate.read())
    print(fillTemplate)

    ## replace text in template
    # replace info
    fillTemplate.replace("STATE_REPLACE", state)
    fillTemplate.replace("STATE_FULL_REPLACE", fullState)
    fillTemplate.replace("LOCATION_REPLACE", locationName)
    fillTemplate.replace("ADDRESS_REPLACE", address)
    fillTemplate.replace("CITY_LAND_REPLACE", city+" // "+land)
    fillTemplate.replace("INFORMATION_REPLACE", bio)
    fillTemplate.replace("VERIFIED_REPLACE", verified)
    fillTemplate.replace("VERIFY_YESNO_REPLACE", verificationYN)

    # replace update and verify html buttons
    updateForm = open("scripts/updateForm.html", "r")
    fillTemplate.replace("SPOTUPDATE_REPLACE", str(updateForm))
    if verificationYN == "No" or verificationYN == "no" or verificationYN == "NO":
        verifyForm = open("scripts/verifyForm.html", "r")
        fillTemplate.replace("SPOTUPDATE_REPLACE", str(verifyForm))
    else:
        fillTemplate.replace("SPOTUPDATE_REPLACE", " ")

    # replace spot specific
    slope = input("What is the slope like? ")
    fillTemplate.replace("SLOPE_REPLACE", slope)
    surface = input("What is the surface like? ")
    fillTemplate.replace("SURFACE_REPLACE", surface)
    cracks = input("What are the cracks like? ")
    fillTemplate.replace("CRACKS_REPLACE", cracks)
    diff = input("What is the difficulty? ")
    fillTemplate.replace("DIFFICULTY_REPLACE", diff)

    # write to file
    newFile.write(fillTemplate)
    newFile.close()

    # completed
    print("The new skatespot file has been created!")

##############

print("Welcome back to your rollerskatespotaus.github.io spot file creator.")
locationName = input("What is the location name? ")
stateIdentified = False

while not stateIdentified:
    state = input("What state (abbreviation) is "+locationName+" in? ")
    if state == "QLD":
        fullState = "Queensland"
        stateIdentified = True
    elif state == "NSW":
        fullState = "New South Wales"
        stateIdentified = True
    elif state == "VIC":
        fullState = "Victoria"
        stateIdentified = True
    elif state == "WA":
        fullState = "Western Australia"
        stateIdentified = True
    elif state == "TAS":
        fullState = "Tasmania"
        stateIdentified = True
    elif state == "NT":
        fullState = "Northern Territory"
        stateIdentified = True
    elif state == "SA":
        fullState = "South Australia"
        stateIdentified = True
    elif state == "ACT":
        fullState = "Australian Capitol Territory"
        stateIdentified = True
    else:
        print("A typo was made.")
    

verificationYN = input("Is it verified? ")
if verificationYN == "Yes":
    verified = "verified"
else:
    verified = "unverified"

address = input("What is the address? ")
city = input("What city is it in? ")
land = input("What Indigenous land is the location on? ")
bio = input("Please submit the spot information: ")

spotType = ["spot", "rink", "park", "store"]
typeIdentified = False

while not typeIdentified:
    submittedType = input("What kind of spot is it? Please type 'spot', 'rink', 'park' or 'store' ")
    if submittedType == spotType[0]:
        selectedType = spotType[0]
        typeIdentified = True
        skatespot()
    elif submittedType == spotType[1]:
        selectedType = spotType[1]
        typeIdentified = True
    elif submittedType == spotType[2]:
        selectedType = spotType[2]
        typeIdentified = True
    elif submittedType == spotType[3]:
        selectedType = spotType[3]
        typeIdentified = True
    else:
        print("A typo was made.")    


# STATE_REPLACE
# STATE_FULL_REPLACE
# LOCATION_REPLACE
# ADDRESS_REPLACE
# CITY_LAND_REPLACE
# INFORMATION_REPLACE
# VERIFIED_REPLACE #VERIFY_YESNO_REPLACE

# SLOPE_REPLACE
# SURFACE_REPLACE
# CRACKS_REPLACE
# DIFFICULTY_REPLACE

# SPOTUPDATE_REPLACE
# SPOTVERIFY_REPLACE



