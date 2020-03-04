message = "it was a birght cold day in April,  and the wind was strong"
count={}#letter(which is represented by "character" in for loop : number of times it shows up

#strings in for loops are "list-like"

for character in message.lower(): #for each character in the string- which is iterated as  list-like
     count.setdefault(character, 0) #count dictionary sets the default value for every character it loops over,
     #if that character is already present in the count dictionary, it will just return the value, aka do nothing in this respect
     count[character] += 1#in the count dictionary, that character passed in (aka count["i"] is show as count = {"i": 0} in the dictionary initially)
     #add 1 to the value of it, (aka if "a" shows up for the second time as a character, count["a"] which has a value of 1 now) add a value of 1 to it
     #now count["a"] has a value of 2 - count = {"a": 2}, if character is "a" again at some point, it will add 1 to that key of "a" -

#print(count)  #print count dictionary, which will show up as (for example) {"a" : 1, "b": 2, "c": 3}

  
