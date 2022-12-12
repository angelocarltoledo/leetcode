def longestCommonPrefix():
    strs = input("Write some words separated by spaces: ").split()

    if not strs:
        return ""
    for i in range(len(strs[0])):
        letter = strs[0][i]
        for j in range(1,len(strs)):
            if i == len(strs[j]) or strs[j][i] != letter:
                return f"The most common prefix is {strs[0][:i]}"
    return f"The most common prefix is {strs[0]}"

print(longestCommonPrefix())