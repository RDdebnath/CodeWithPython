word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(word in data):
        print("FOUND")

    else:
        print("NOT FOUND")