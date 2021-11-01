def alphabet(received):
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        if i in received:
            print("String Contains A Vowel")
            break
        else:
            print("String Contains Only Consonant")
            break


theAlpha = input("Enter An Alphabet :")
alphabet(theAlpha)


def even_odd_sort(arr):
    odd_array = []
    even_array = []
    for i in arr:
        if i % 2 == 1:
            odd_array.append(i)
        else:
            even_array.append(i)
    result = even_array + odd_array
    return result


theArr = [3, 2, 18, 0, 7, 6]
print(even_odd_sort(theArr))


cache = {}


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError("Should Be A Positive Number")
    elif type(n) != int:
        raise TypeError("Should Be An Integer")
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result


print(fibonacci(3))


stringer = "welcometopython"
k = 3
subber = []
for i in range(len(stringer)):
    if i + k != len(stringer) + 1:
        subbed = stringer[i: i + k]
        subber.append(subbed)
    else:
        break
subber.sort()
print(subber)
