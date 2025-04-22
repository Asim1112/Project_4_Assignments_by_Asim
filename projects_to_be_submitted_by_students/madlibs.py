# MADLIBS PROJECT



name = input("Name: ")
thing = input("Thing: ")
animal = input("Animal: ")
sound = input("Sound: ")
verb = input("Verb: ")




#  USING F STRING
madlib = f"{name} went to the beach and brougth a {thing}. Sunddenly, a {animal} prepared and shouted, '{sound}!' Everyone started to {verb}, and the beach party turned into a zoo!"


# USING CONCATENATION
madlib2 = name + " went to the beach and brought a " + thing + ". Suddenly, a " +  animal + " prepared and shouted, " + "'" + sound + "!'" + " Everyone started to " + verb + ", and the beach party turned into a zoo!"




print(madlib)
print(madlib2)

