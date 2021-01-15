def strStr(haystack, needle):
    try:
        return haystack.index(needle) if needle != "" else 0
    except ValueError:
        return -1

print(strStr("aaaaa", "bba"))