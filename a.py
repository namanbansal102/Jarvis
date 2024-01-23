print("The next Palindorme Problem")
num = "2133"


def cal(*args):
    for i in args:
        
        for n in range(100):
            k_num = int(i)+n
            new_num = str(k_num)[::-1]
            if (k_num == int(new_num)):
                print(f"Your Palidorme is {k_num} ")
                
                break
            
    else:
        print("Function Completed")


test_cases = int(input("Enter Number Of Test Cases: "))
lst = []
for i in range(test_cases):
    inp = input("Enter The Number You Want Palidrome: ")
    lst.append(inp)
cal(*lst)

