count = 0
with open("practice1.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for item in nums:
        if(int(item) % 2 == 0):
            count +=1

print(count)