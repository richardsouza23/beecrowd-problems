
def get_calls_and_result(x):
    a_result = a_calls = b_calls = 0
    b_result = 1

    if x == 0:
        return a_result, a_calls
    elif x == 1:
        return b_result, b_calls
    else:

        for i in range(x-1):
            temp = a_result
            a_result = b_result
            b_result += temp

            temp2 = a_calls
            a_calls = b_calls
            b_calls += temp2 + 2
        
        return b_result, b_calls


inputCount = int(input())

for i in range(inputCount):

    x = int(input())

    result, num_calls = get_calls_and_result(x)

    print("fib({x}) = {num_calls} calls = {result}".format(x = x, num_calls = num_calls, result = result))
    