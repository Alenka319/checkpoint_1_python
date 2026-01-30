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