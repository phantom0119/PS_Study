# 백준 25628 햄버거 만들기 (2022 충남대)   브론즈4
# 수학, 사칙연산

'''
그릇 위에 빵을 놓는다.
빵 위에 패티를 올린다.
패티 위에 다시 빵을 올려서 햄버거를 완성시킨다.
'''
B, P = map(int, input().split())
B = B//2

print(min(B, P))