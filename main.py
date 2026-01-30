# 1 задание с функцией get_sum
def get_sum(a, b):
    return a + b


# 2 задание с функцией count_capital_letters
def count_capital_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count


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



# 4 задание с функцией get_odd_count
def get_odd_count(s):
    count = 0
    for char in s:
        digit = int(char)
        if digit % 2 == 0 and digit != 0:
            count += 1
    return count



# 5 задание с функцией check_access 
def check_access(has_keycard, has_fingerprint, is_alarm, is_daylight):
    if is_alarm:
        return False
    if has_fingerprint:
        return True
    if has_keycard and is_daylight:
        return True
    return False

