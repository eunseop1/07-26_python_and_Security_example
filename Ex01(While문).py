# while 반복문
"""
조건이 참인 동안 반복 실행한다
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
"""
height = int(input('몇줄?'))

i = 0
while i < height:
    print(" " *(height - i), end="")
    print("*" * (i * 2 - 1))
    i += 1