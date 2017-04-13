import unittest

def to_camel_case(text):
    words = text.replace('_', '-').split('-')

    if words:
        return words[0] + "".join([str.capitalize(word) for word in words[1:]])
    else:
        return ""

class CamelTest(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(to_camel_case(""), "")

    def testFirstUpper(self):
        self.assertEqual(to_camel_case("I_Am_the_Champion"), "IAmTheChampion")

    def testFirstLower(self):
        self.assertEqual(to_camel_case("i-am-awesome"), "iAmAwesome")

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))

unittest.main()
