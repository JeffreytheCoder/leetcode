# not work
def myAtoi(s):
    isFalse = False
    isSigned = False
    isZeroed = False
    nums = '0123456789'
    new_s = ''
    for char in s:
        if char == '-' and isSigned == False and isZeroed == False:
            isFalse = True
            isSigned = True
        elif char == '+' and isSigned == False and isZeroed == False:
            isSigned = True
        elif char == ' ':
            pass
        elif new_s == '' and char == '0':
            isZeroed = True
        elif char in nums:
            new_s += char
        else:
            if (new_s == ''):
                return 0
            else:
                return new_s
    if new_s == '':
        return 0
    new_int = -int(new_s) if isFalse else int(new_s)
    if new_int < pow(2, 31) - 1:
        if new_int > pow(-2, 31):
            return new_int
        else:
            return pow(-2, 31)
    else:
        return pow(2, 31) - 1

print(myAtoi("42"))
print(myAtoi("    -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("3.14159"))
print(myAtoi("21474836460"))
print(myAtoi("00000-42a1234"))
print(myAtoi("  -0012a42"))
print(myAtoi("  0000000000012345678"))
print(myAtoi("00000-42a1234"))

print(myAtoi("  -0012a42"), 0)
print(myAtoi("4193 with words"), 4193)

print(not "-0012")

print(" ".isdigit())