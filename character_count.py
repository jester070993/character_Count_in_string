import pprint

message = "It was a birght cold day in April, and the wind was strong"
longMes = "A TXT file is a standard text document that contains unformatted text. It is recognized by any text editing or word processing program and can also be processed by most other software programs. ... TXT files are useful for storing information in plain text with no special formatting beyond basic fonts and font styles."
count={}#letter(which is represented by "character" in for loop : number of times it shows up
#count is a dictionary

#strings in for loops are "list-like" aka you can access each character in a string individually using a for loop 

for character in longMes.lower(): #for each character in the string- which is iterated as  list-like
     count.setdefault(character, 0) #count dictionary sets the default value for every character it loops over,
     #if that character is already present in the count dictionary, it will just return the value, aka do nothing in this respect
     count[character] += 1#in the count dictionary, that character passed in (aka count["i"] is show as count = {"i": 0} in the dictionary initially)
     #add 1 to the value of it, (aka if "a" shows up for the second time as a character, count["a"] which has a value of 1 now) add a value of 1 to it
     #now count["a"] has a value of 2 - count = {"a": 2}, if character is "a" again at some point, it will add 1 to that key of "a" -

pprint.pprint(count)  #print count dictionary, which will show up as (for example) {"a" : 1, "b": 2, "c": 3}
#pprint module pprint method prints list or dictionaries values nicely,
#in alphabeticcal order rather than just the order they show up in

