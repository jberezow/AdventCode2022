import numpy as np

source = "dec4.txt"
with open(source,"r") as file:
  data = file.readlines()

def parse_ranges(line):
  range1, range2 = line.split(",")
  r1a, r1b = [int(x) for x in range1.split("-")]
  r2a, r2b = [int(x) for x in range2.split("-")]
  if r1a <= r2a:
    if r1b >= r2b:
      return(1)
  if r2a <= r1a:
    if r2b >= r1b:
      return(1)
  return(0)

# Part 1
score = 0
for line in data:
  score += parse_ranges(line)

print(score)

# Part 2
def parse_ranges(line):
  range1, range2 = line.split(",")
  r1a, r1b = [int(x) for x in range1.split("-")]
  r2a, r2b = [int(x) for x in range2.split("-")]
  r1 = range(r1a, r1b+1)
  r2 = range(r2a, r2b+1)
  print(r1)
  print(r2)
  sames = np.intersect1d(r1, r2)
  if sames.size > 0:
    return(1)
  return(0)

score = 0
for line in data:
  score += parse_ranges(line)

print(score)