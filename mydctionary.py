mydict = {"Adduct":"To move a part of the body towards the middle of the body or towards another body part",
         "Backstabbing":"The act of saying harmful or unpleasant things about a person when they are not present",
         "Candlewick":"Thick, soft material with raised areas of short threads on the surface",
         "Dabble":"To take a slight and not very serious interest in a subject, or try a particular activity for a short period",
         "Enthrone":"To put a king, queen, etc. through the ceremony of sitting on a throne in order to mark the official beginning of their period in power"}
print(mydict.keys())
key = input("Select the word from above the mentioned list: ")
print("The meaning of", key, "is", mydict[key])