import sys
sys.stdin = open('workshop.txt')
T = 10
for tc in range(1, T+1):
   N = int(input())
   data = list(input())
   stack = []
   arr = []
   val1 = {'+': 1, '*': 2, '(': 3} # 넣을때
   val2 = {'+': 1, '*': 2, '(': 0} # 스택 안
   for i in range(N):
       if data[i].isdigit():
           arr.append(data[i]) # 숫자
       else: # 연산자
           if not stack:
               stack.append(data[i])

           elif stack:
               if data[i] == ')':
                   while stack[-1] != '(':
                       arr.append(stack.pop())
                   stack.pop()
               elif val1[data[i]] > val2[stack[-1]]:
                   stack.append(data[i])
               else:
                   while val1[data[i]] <= val2[stack[-1]]:
                       arr.append(stack.pop())
                   stack.append(data[i])
   print(arr)
   for i in range(len(arr)):
       if arr[i].isdigit():
           stack.append(arr[i])
       else:
           num2 = int(stack.pop())
           num1 = int(stack.pop())
           if arr[i] == "+":
               result = num2 + num1
           elif arr[i] == '*':
               result = num2 * num1
           stack.append(str(result))
   print('#{} {}'.format(tc, stack[0]))