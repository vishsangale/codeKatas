from collections import Counter


def compress(data):
    in_len = len(data)
    counter = Counter(data)
    if 2*len(counter) >= in_len:
        return data

    out = []

    last_char = None
    count = 0
    for char in data:
        if last_char == char:
            count += 1
        else:
            if last_char is not None:
                out.append(last_char + str(count))
            last_char = char
            count = 1
    out.append(last_char + str(count))

    return "".join(out)


print(compress("abc"))
print(compress("aabc"))

print(compress("aabccccaa"))