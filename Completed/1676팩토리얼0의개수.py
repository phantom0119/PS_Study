# 백준 1676 팩토리얼 0의 개수   실버5
# 수학, 임의 정밀도/ 큰 수 연산
# http://daplus.net/math-%EC%9E%84%EC%9D%98-%EC%A0%95%EB%B0%80%EB%8F%84-%EC%82%B0%EC%88%A0-%EC%84%A4%EB%AA%85/

'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
'''
from sys import stdin
inputF = stdin.readline
N = int(inputF())
T = 125 # 5의 제곱수 중에서 가능한 최대
ret = 0
while True:
    ret += N//T
    T /= 5
    if T == 1:
        break

print(int(ret))

# 5! = 120  -> 1개   
# 10! = 362800 -> 2개 
# 15! = 1307674368000  -> 3개 
# 20! = 2432902008176640000 -> 4개
# 25! = 6개


# 5, 25, 125까지가 최대 (  0 <=  N  <=  500)

# 5 - 1개
# 5, 10 - 2개
# 5, 10, 15 - 3개
# 5, 10, 15, 20 - 4개
# 5, 10, 15, 20, 25(5x5) - 6개
# 5, 10, 15, 20, 25(5*5), 30 - 7개?