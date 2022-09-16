from operator import le


def solution(s):
    
    array = [letter for letter in s]

    new_array = []

    for _ in array:

        if len(array) == 0:
            break
        try:
            new_array.append(array[0] + array[1])
        except IndexError:
            new_array.append(array[0] + "_")

        array = array[2:]

    
    return new_array


s1 = "asdfadsf"
s2 = "asdfads"
s3 = ""
s4 = "x"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))