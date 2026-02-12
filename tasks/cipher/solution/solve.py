with open("/app/encrypted.txt") as f:
    text = f.read().strip()
result = []
for c in text:
    if "a" <= c <= "z":
        result.append(chr((ord(c) - ord("a") - 15) % 26 + ord("a")))
    elif "A" <= c <= "Z":
        result.append(chr((ord(c) - ord("A") - 15) % 26 + ord("A")))
    else:
        result.append(c)
with open("/app/decrypted.txt", "w") as f:
    f.write("".join(result))
