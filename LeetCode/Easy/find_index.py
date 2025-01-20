def strStr(haystack, needle):
    length_of_needle = len(needle)
    haystack_list = list(haystack)
    i = 0
    while i <= len(haystack):
        check = haystack[i:i+length_of_needle]
        if  check == needle:
            return i
        else:
            i = i + 1
    
    return -1

print(strStr("butsad", "sad"))