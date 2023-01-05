"""
param: s(string type)

최댓값과 최솟값 함수
-> 문자열 파라미터 s에서 최솟값과 최댓값 구하기
"""
def solution(s):
    array = s.split()
    min = int(array[0])
    max = int(array[0])
    for value in array:
        value = int(value)
        if min > value:
            min = value
        if max < value:
            max = value
    return f"{min} {max}"