#Today i went to the garden, i saw a beautiful peacocke that was dancing.


place = input("Enter a place: ").lower()
adjective = input("Enter an adjective: ").lower()
noun = input("Enter a noun: ").lower()
verb = input("Enter a verb: ").lower()


mad_libs = "Today i went to the {} ".format(place) + "i saw a {} ".format(adjective) + "{} ".format(noun) + "that was {} ".format(verb) + " ."

print(mad_libs)
