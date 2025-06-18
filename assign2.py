alpha = 0
num = 0

for i in list("Brudite"):
    if i.isalpha():
        alpha += 1
    else:
        num += 1

print(f"total alpha: {alpha}")
print(f"total nums: {num}")