# rollerskatespots new spot file creator

# todo: spotTemplate.html doesn't exist apparently in the same directory

##########

def skatespot():
    print("Creating new skatespot...")
    
    # read template file
    readTemplate = open("spotTemplate.html", "r")
    
    # create new file
    fileName = locationName.replace(" ", "")

    ### if file already exists, delete context and write to it
    newFile = open(fileName+".html", "x")
    
    # write template text to file
    newFile.write(str(readTemplate))

    ## replace text in template
    # replace info
    newFile.replace(STATE_REPLACE, state)
    newFile.replace(STATE_FULL_REPLACE, fullState)
    newFile.replace(LOCATION_REPLACE, location)
    newFile.replace(ADDRESS_REPLACE, address)
    newFile.replace(CITY_LAND_REPLACE, city+" // "+land)
    newFile.replace(INFORMATION_REPLACE, bio)
    newFile.replace(VERIFIED_REPLACE, verified)
    newFile.replace(VERIFY_YESNO_REPLACE, verificationYN)

    # replace update and verify html buttons
    updateForm = open("updateForm.html", r)
    newFile.replace(SPOTUPDATE_REPLACE, updateForm)
    if verificationYN == no:
        verifyForm = open("verifyForm.html", r)
        newFile.replace(SPOTUPDATE_REPLACE, verifyForm)
    else:
        newFile.replace(SPOTUPDATE_REPLACE, " ")

    # replace spot specific
    slope = input("What is the slope like? ")
    newFile.replace(SLOPE_REPLACE, slope)
    surface = input("What is the surface like? ")
    newFile.replace(SURFACE_REPLACE, surface)
    cracks = input("What are the cracks like? ")
    newFile.replace(CRACKS_REPLACE, cracks)
    diff = input("What is the difficulty? ")
    newFile.replace(DIFFICULTY_REPLACE, diff)

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



