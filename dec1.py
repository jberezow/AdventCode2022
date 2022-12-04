import numpy as np

source = "dec1.txt"
with open(source,"r") as file:
  data = file.readlines()

elf_sums = []
current_sum = 0

for line in data:
  if line == "\n":
    elf_sums.append(current_sum)
    current_sum = 0
  else:
    current_sum += int(line)

# Part A
print(max(elf_sums))

# Part B
elf_sums = np.sort(elf_sums)
total = np.sum(elf_sums[-3:])
print(total)


