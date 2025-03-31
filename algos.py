def reverse_string(str):
    return str[::-1]

def alternate_cases(str):
    result = ''
    for i in range(0, len(str)):
        if i % 2:
            result += str[i].upper()
        else:
            result += str[i].lower()
    return result

def starts_with_a_vowel(str):
    return True if str[0] in ['a','e','i','o','u'] else False

def add_alternating_indices(arr, start=0):
    if start >= len(arr): return False
    sum = 0
    for i in range(start, len(arr), 2):
        sum += arr[i]
    return sum