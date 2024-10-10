
n = input("Digite o número: ")
newi = ""
f = len(n)  -1

for i in range(f, -1, -1):

    newi += str(n[i])

print(f"{newi} newi")
print(f"{n} origem")
