"""
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

            472  ----  (1)
           *385  ----  (2)
_______________
           2360  ----  (3)
          3776   ----  (4)
         1416    ----  (5)
_______________
         181720  ----  (6)

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 
(3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

"""

def calc(n1, n2):
    print(n1 * n2)
num1 = input()
num2 = input()

calc(int(num1), int(num2[2]))
calc(int(num1), int(num2[1]))
calc(int(num1), int(num2[0]))
calc(int(num1), int(num2))
