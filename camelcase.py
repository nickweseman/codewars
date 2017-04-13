def to_camel_case(text):
    words = text.replace('_','-').split('-')

    if words:
        return words[0] + "".join([str.capitalize(word) for word in words[1:]])
    else:
        return ""


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))