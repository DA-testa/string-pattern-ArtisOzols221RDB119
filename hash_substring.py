def read_input():
    iorf = input().strip()
    if iorf != "I" and iorf != "F":
        raise ValueError("Input not I or F")
    if iorf == "I":
        find = input()
        text = input()
    elif iorf == "F":
        try:
            with open("./tests/06") as file:
                find = file.readline()
                text = file.readline()
        except FileNotFoundError:
            print("No file found")
            exit()
    return find, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(find, text):
    n=[]
    findl = len(find)
    textl = len(text)
    hash_find = hash(find)
    hash_text = hash(text[:findl])
    for i in range(0, 1+textl-findl):
        if hash_find == hash_text and find == text[i:findl+i]:
            n.append(i)
        if i < textl - findl:
            hash_text = hash(text[1+i:1+findl+i])
    return n

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
