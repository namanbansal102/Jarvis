import random
print("'Rohan Das is a Fraud Problem")
lst=[]
def rohanMultiplication(num):
    global lst
    lst=[(n+1)*num for n in range(10) ]
    lst[random.randint(1,11)]=random.randint(num+10,num+20)
    return lst
def isCorrect(table,*number):
    print("Correction is Running")
    correct_lst=[(n+1)*table for n in range(10) ]
    
    for index,item in enumerate(correct_lst):
        if(item==number[index]):
            pass
        elif correct_lst==number:
            return None
        else:
            k=f"In multiplication Table of {table} Wrong at {index+1}*{table}!={number[index]}"
            return k
            

rohanMultiplication(6)

print("Number Index Wrong is",isCorrect(6,*lst))




