# python 3.6
def solution(N):
    if not isinstance(N, (int, float, bytearray)):
        return "Hello it is not number"
    try:
        if 1 <= N <= 2147483647:
            return len(max(format(N, 'b').strip('0').split('1')))
        else:
            raise ValueError("Value out or range [1..2,147,483,647]")
    except ValueError as valueerror:
        return valueerror


print(solution(17))
print(solution('17'))
print(solution(21474836439))