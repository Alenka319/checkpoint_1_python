# 1 задание с функцией get_sum
def get_sum(a, b):
    return a + b
print(get_sum(1, 2))
print(get_sum(2, 2))
print(get_sum(-5, 10))


# 2 задание с функцией count_capital_letters
def count_capital_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count

print(count_capital_letters("Hello World"))
print(count_capital_letters("   A   "))
print(count_capital_letters("hello world"))
print(count_capital_letters("PYTHON"))


# 3 задение с функцией decode_string
def decode_string(s):
    s_lower = s.lower() 
    result = ""
    
    for char in s_lower:
        count = 0
        
        for check_char in s_lower:
            if check_char == char:
                count += 1

        if count == 1:
            result = result + "("
        else:
            result = result + ")"
    
    return result

print(decode_string("din"))
print(decode_string("recede"))
print(decode_string("Success"))
print(decode_string("(( @"))
print(decode_string("aAabBc"))


# 4 задание с функцией get_odd_count
def get_odd_count(s):
    count = 0
    for char in s:
        digit = int(char)
        if digit % 2 == 0 and digit != 0:
            count += 1
    return count

print(get_odd_count("2468"))
print(get_odd_count("13579"))
print(get_odd_count("01234567"))

print(get_odd_count("0022446688"))
print(get_odd_count("1029384756"))
print(get_odd_count("000"))
print(get_odd_count(""))


# 5 задание с функцией check_access 
def check_access(has_keycard, has_fingerprint, is_alarm, is_daylight):
    if is_alarm:
        return False
    if has_fingerprint:
        return True
    if has_keycard and is_daylight:
        return True
    return False

print("Тест 1 (Ключ, день, нет тревоги):", check_access(True, False, False, True))   
print("Тест 2 (Ключ, ночь, нет тревоги):", check_access(True, False, False, False))  
print("Тест 3 (Палец, ночь, нет тревоги):", check_access(False, True, False, False)) 
print("Тест 4 (Палец, день, но ЕСТЬ тревога):", check_access(False, True, True, True)) 
print("Тест 5 (Ключ И палец, день, нет тревоги):", check_access(True, True, False, True)) 
print("Тест 6 (Ничего нет):", check_access(False, False, False, True))