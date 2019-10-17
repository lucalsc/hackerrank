#You are given a string and your task is to swap cases. 
#In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(string):
    s_list = [i.lower() if i.isupper() else i.upper() for i in string]
    new_string = ''.join(s_list)
    return new_string

if __name__ == '__main__':
    string = input()
    print(swap_case(string))