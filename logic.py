def alternate(s):

    new_font = ''

    for i in range(len(s)):
        if i % 2 == 0 or i == 0:
            up = s[i].upper()
            new_font += up
            
        else:
            low = s[i].lower()
            new_font += low
    
    return new_font

print(alternate("words"))