import math

def __task1__(x,y):
    exponent = 0
    answer = (((x**7)-math.sin(y))**5 + math.sin(x) + (((13*((y)**4))-x**6)/((92*(x**3))+math.tan(y))) + y**6 + math.e**y)
    # if (answer > 0):
    #     while (answer % 10 == 0):
    #         exponent += 1
    #         answer %= 10
    return answer

print("f(36,-52) = {:e}".format(__task1__(36,-52)))
print("f(-31,29) = {:e}".format(__task1__(-31,29)))

def __task2__ (x):
    if x < -66:
        answer = x**7 + x**5 + 53
    if -66 <= x < -36:
        answer = 72*x**7 - math.e**x + 20
    if -36 <= x < 63:
        answer = x**5 - x**7
    if 63 <= x < 97:
        answer = x**5 + x**7
    if 97 <= x:
        answer = 76*x - ((x**8)/74)

    return answer

print("f(-71) = {:e}".format(__task2__(-71)))
print("f(36) = {:e}".format(__task2__(36)))