wduw=(input("what you wanna use encoder or decoder:"))
if wduw=="encoder":
    print("you choose encoder")
    msg1=(input("enter the code you wanna encode:"))
    print("the code you wanna encode is:",msg1)
    print("your encoded code is:", end="")
    for i in msg1:
        print(chr(ord(i)+3), end="")
    print() 
elif wduw=="decoder":
    print("you choose decoder")
    msg2=(input("enter the code you wanna decode:"))
    print("the code you wanna decode is:",msg2)
    print("your decoded code is:", end="")
    for i in msg2:
        print(chr(ord(i)-3), end="")        
    print()
else:    
    print("you choose nothing")

