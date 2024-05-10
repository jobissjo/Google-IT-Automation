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
