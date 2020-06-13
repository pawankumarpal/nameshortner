#taking input
line = input("enter the name : ").lower()
#converting string into list
last=list(line.split(" ")) 
#taking last word from the line
ll="".join(last[-1])
#splitting elements of line
words = line.split()
#loop for printing element at position 0
letters = [word[0] for word in words]
#poping last element in letter
letters.pop(-1)
#printing output using concatinating and upper 
print (".".join(letters).upper()+"."+last[-1].capitalize())

