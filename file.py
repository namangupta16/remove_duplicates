def remove_duplicates(string):
    seen = set()
    result=[]
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
            
    return ''.join(result)


remove_duplicates('hello')
remove_duplicates('icecream sandwitch is good good')