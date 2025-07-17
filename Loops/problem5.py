num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 25

i = 0 
while i < len(num):
    if(num[i] == x):
        print("FOUND the idx", i)
    i += 1