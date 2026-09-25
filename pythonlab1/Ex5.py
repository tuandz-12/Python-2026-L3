#Ex5
Colors_list = ["Blue","blue","Red","red"]
n = input("What is your favourite color?")
if n in Colors_list:
    a=Colors_list.index(n)
    print("Your color is at index", a  ,"in my list")  
else:
    print("Sorry, I could not find your color")  