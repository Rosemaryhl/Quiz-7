#Rosemary Hoffman
def hash_spam(string, target):
    total=0
    index=0
    while index<len(string):
        for ch in string:
            if ch=="#":
                total=total+1
                index=index+1
            else:
                index=index+1
        if total>=4:
            print("this tweet will be considered as a spam!")
        else:
            return None
hash_spam("#wow #this #is #so #cool", "#")
hash_spam("#wow #this #is","#")
