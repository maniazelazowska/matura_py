#PURE HERESY AHEAD - PROCEED AT YOUR OWN RISK
from collections import Counter

file = open("dane_anagramy.txt", "r")
results = open("wyniki_anagramy4b.txt", "w")

#eye closing HIGHLY advised
def zadanie4b():
    numbers = []
    frequency = 0
    for lines in file:
        for line in lines.split("\n"):
            for number in line.split():
                numbers.append(sorted(number))
    leader = max(numbers,key=numbers.count)
    frequency = numbers.count(leader)
    results.write(f"ZAD 4 b)\nMaksymalnie liczb, z ktorych kazde dwie to anagramy cyfrowe:\n{frequency}\n\n")
  
#HERESY END  
zadanie4b()
file.close()
results.close()
