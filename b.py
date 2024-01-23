print("Palondrimfy the List")
lst=[1,6,87,43,43,100,434,3434,133,10,9]
for index,number in enumerate(lst):
    if(number>10):
        for n in range(1000):
            k_num = int(number)+n
            new_num = str(k_num)[::-1]
            if (k_num == int(new_num)):
                print(f"Your Palidorme is {k_num} ")
                lst[index]=k_num
                break
print(lst)
