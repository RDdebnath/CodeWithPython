def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

cars = ["thar", "lamborgini", "bugatti", "mustang"]

print_list(cars)