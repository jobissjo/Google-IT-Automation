import re

result = re.search(r"aza", 'Plaza')
print(result)


result1 = re.search(r"p.....n", "penguin")
print(result1)

pattern = r"^p.*n$"

print(re.search(pattern, "Penguin", re.IGNORECASE))


import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True            


##############################################################

print(re.search(r'[a-z]obi', 'jobi is a good boy'))

print(re.findall(r"cat|dog", "I like both dogs and cats."))
# print(re.findall(r"cat|dog", "I like both dogs and cats."))
print(re.search(r"[^a-zA-Z]", "I like both dogs and cats."))

###############################################################

print(re.search(r"Py.*n", "Pygmalion"))


print(re.search(r"\w*", "Pygmalion is what we do"))
print(re.search(r"\w*", "Pygmalion_is_what_we_do"))


import re

def repeating_letter_a(text):
    result = re.search(r"[aA].*[aA]", text)
    return result is not None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

import re

def check_character_groups(text):
    result = re.search(r"\w+\s+\w+", text)
    return result is not None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))


import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable")) #None
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1")) #None