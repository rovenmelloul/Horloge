
def search(str:str, researched_str:str)->int:
    count = 0
    for i in range(len(str)):
        if researched_str.lower() is str[i]:
            count +=1
    return count

print(search("Hellow word", "w"))
