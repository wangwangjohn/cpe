r = {'e': 'q', 'd': 'a', 'c': 'z', 'r': 'w', 'f': 's', 'v': 'x', 't': 'e', 'g': 'd', 'b': 'c', 'y': 'r', 'h': 'f', 'n': 'v', 'u': 't', 'j': 'g', 'm': 'b', 'i': 'y', 'k': 'h', ',': 'n', 'o': 'u',
     'l': 'j', '.': 'm', 'p': 'i', ';': 'k', '/': ',', '[': 'o', "'": 'l', ']': 'p', '2': '`', '3': '1', '4': '2', '5': '3', '6': '4', '7': '5', '8': '6', '9': '7', '0': '8', '-': '9', '=': '0', '\\': '['}
# 建表左邊寫內容，右邊寫對應的內容
while (True):
    str = input()
    str2 = str.lower()  # 大寫轉小寫
    result = ""
    for i in str2:
        if i in r:
            result += r.get(i, i)
        else:
            result += i
    print(result)
