with open("sri",'w+') as f:
    f.write("Hello Srinadh")
with open("sri",'r+') as f:
    print(f.read())
with open("sri",'a') as f:
    f.write("How are you man")
with open("sri",'r+') as f:
    print(f.read())