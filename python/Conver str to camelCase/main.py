def to_camel_case(text):
    #your code here

    newStr = ""
    
    text = list(text)

    if len(text) == 0:
        return ""
    else:
        for i in range(len(text)):
            
            if text[i] == "-" or text[i] == "_":
                text[i + 1] = text[i + 1].upper()
                continue

            newStr += text[i]
                
    return newStr


str1 = ""
str2 = "the_stealth_warrior"
str3 = "The-Stealth-Warrior"
str4 = "A-B-C"

print(to_camel_case(str1))
print(to_camel_case(str2))
print(to_camel_case(str3))
print(to_camel_case(str4))