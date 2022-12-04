import numpy as np
import string
lower = dict(zip(string.ascii_lowercase, range(1,27)))
upper = dict(zip(string.ascii_uppercase, range(27,53)))

master = {}
master.update(lower)
master.update(upper)

source = "dec3.txt"
with open(source,"r") as file:
  data = file.readlines()

def parse_items(line):
  length = len(line)
  item1 = line[:length//2]
  item2 = line[length//2:]
  return(item1, item2)

def compare_items(item1, item2):
  for c in item1:
    if c in item2:
      return(c)
  return(" ")

# Part 1
score = 0
for line in data:
  item1, item2 = parse_items(line)
  priority = compare_items(item1, item2)
  score += master[priority]

print(score)

# Part 2
def parse_group(elf1, elf2, elf3):
  for c in elf1:
    if c in elf2:
      if c in elf3:
        return(c)
  return(" ")

score = 0
for i in range(0, len(data), 3):
  elf1 = data[i]
  elf2 = data[i+1]
  elf3 = data[i+2]
  priority = parse_group(elf1, elf2, elf3)
  score += master[priority]
print(score)
