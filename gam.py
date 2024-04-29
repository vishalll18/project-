print("Welcome to eligibilty test")
print("---------------------------")
name=input("Enter your name ")
num=input("Enter your age")

if(int(num)>18):
    print("Your are eligible for driving")
elif(int(num)<18 or int(num)==18 ):
    print("your are not eligible for driving")
    #it can also be in written in one line
