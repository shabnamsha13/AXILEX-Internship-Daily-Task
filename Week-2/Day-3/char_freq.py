#find frequency of each character
text = input("Enter a string: ")
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character Frequency:")
for key in freq:
    print(key, ":", freq[key])
