import numpy as np

source = "dec2.txt"
with open(source,"r") as file:
  data = file.readlines()

scores = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

results = {
  "W": 6,
  "D": 3,
  "L": 0
}

def rps(elf, me):
  score = 0
  if elf == "A":
    if me == "X":
      score += results["D"]
    elif me == "Y":
      score += results["W"]
    elif me == "Z":
      score += results["L"]
    else:
      print("Me broken")
  elif elf == "B":
    if me == "X":
      score += results["L"]
    elif me == "Y":
      score += results["D"]
    elif me == "Z":
      score += results["W"]
    else:
      print("Me broken")
  elif elf == "C":
    if me == "X":
      score += results["W"]
    elif me == "Y":
      score += results["L"]
    elif me == "Z":
      score += results["D"]
    else:
      print("Me broken")
  else:
    print("Elf broken")
  score += scores[me]
  return(score)

# Part 1
total_score = 0
for line in data:
  elf = line[0]
  me = line[2]
  total_score += rps(elf,me)

print(total_score)

# Part 2
results = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

def pick(elf, res):
  score = 0
  if elf == "A":
    if res == "X":
      score += scores["Z"]
    elif res == "Y":
      score += scores["X"]
    elif res == "Z":
      score += scores["Y"]
    else:
      print("Res broken")
  elif elf == "B":
    if res == "X":
      score += scores["X"]
    elif res == "Y":
      score += scores["Y"]
    elif res == "Z":
      score += scores["Z"]
    else:
      print("Res broken")
  elif elf == "C":
    if res == "X":
      score += scores["Y"]
    elif res == "Y":
      score += scores["Z"]
    elif res == "Z":
      score += scores["X"]
    else:
      print("Res broken")
  else:
    print("Elf broken")
  score += results[res]
  return(score)

total_score = 0
for line in data:
  elf = line[0]
  res = line[2]
  total_score += pick(elf,res)

print(total_score)
