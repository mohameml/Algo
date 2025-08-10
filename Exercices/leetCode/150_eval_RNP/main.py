from typing import List 

def evalRPN(tokens: List[str]) -> int:
    stack = []
    ops = {
        "+" : lambda x , y : x + y ,
        "-" : lambda x , y : x - y, 
        "*" : lambda x , y : x * y , 
        "/" : lambda x , y : x / y 
    }

    for token in tokens : 
        if token not in ["+" , "-" , "*" , "/"]:
            stack.append(int(token))
        else : 
            right = stack.pop()
            left = stack.pop()
            stack.append(int(ops[token](left , right)))
    return stack[0]     


#  Test : 
tokens = ["4","13","5","/","+"]

res = evalRPN(tokens)
print(res) # 6

