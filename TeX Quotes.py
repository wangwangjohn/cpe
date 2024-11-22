while True:
    try:
        n = input()
    except EOFError:
        break
    c = 0
    a = []
    # 尋訪字串每個字元
    for i in n:
       # 當尋訪到"時候以c判斷當前"是否為第一個"
        if i == "\"":
            if c == 0:
                a.append("``")
                c = 1
            else:
                a.append("''")
                c = 0
        else:
            a.append(i)
    result = "".join(a)
    print(result)
