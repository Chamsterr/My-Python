def find_missing_letter(chars):    
    return chr([ord(chars[x]) + 1 for x in range(len(chars) - 1) if ord(chars[x]) - ord(chars[x+1]) != -1][0])

print(find_missing_letter(['a', 'b', 'c', 'e']))