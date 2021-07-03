from collections import deque
def division(arr):
    arr_de=deque(arr)
    u,v="",""
    left,right=0,0
    while arr_de:
        u += arr_de.popleft()
        if u[-1]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            break
    v = ''.join(list(arr_de))
    return u, v
def reverse(u):  # 뒤집기   그냥 reverse쓰면 안됨
    return ''.join([')' if s == '(' else '('for s in u])
def recursive(string): #######반복
    if string == '':
        return ''
    u,v=division(string)
    if correct(u):
        return u+recursive(v)
    else:
        rev=u[1:-1]
        return '('+recursive(v)+')'+reverse(u[1:-1])

def correct(corarr):
    arr=[]
    for sub in corarr:
        if sub == ')':
            if len(arr)==0:
                return False
            else:
                arr.pop()
        else:
            arr.append(sub)
    if len(arr)==0:
        return corarr
def solution(p):
    return p if correct(p) else recursive(p)


####################다른 풀이
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False #불균형
        if c==0: #############균형
            if r: #올바른
                return p[:i+1]+solution(p[i+1:])
            else: #불균형
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))