#Rosemary Hoffman Quiz 7
def count_hashtag(string, target):
    total=0
    index=0
    while index<len(string):
        for ch in string:
            if ch=="#":
                total=total+1
                index=index+1
            else:
                index=index+1
    return total


print(count_hashtag("#wow #smc","#"))
