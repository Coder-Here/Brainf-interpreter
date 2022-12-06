while True:
    get = input("bf:").strip()
    cell = 0
    cells = [0 for _ in range(1000000)]
    ip = 0
    while True:
        if ip >= len(get):
            break
        if get[ip] == '>':
            cell = (cell + 1) % len(cells)
        elif get[ip] == '<':
            cell = (cell - 1) % len(cells)
        elif get[ip] == '+':
            cells[cell] = (cells[cell] + 1) % 256
        elif get[ip] == '-':
            cells[cell] = (cells[cell] - 1) % 255
        elif get[ip] == '.':
            print(chr(cells[cell]))
        elif get[ip] == ',':
            inp = input()
            if inp:
                cells[cell] = ord(inp[0])
        elif get[ip] == '[':
            open = []
            open.append(ip)
            if cells[cell] == 0:
                find = ip
                while True:
                    find += 1
                    if get[find] == '[':
                        open.append(find)
                    elif get[find] == ']':
                        if len(open) > 1:
                            open.pop()
                        elif len(open) == 1:
                            ip = open.pop()
                            break
        elif get[ip] == ']':
            close = [] 
            close.append(ip)
            if cells[cell] != 0:
                find = ip
                while True:
                    find -= 1
                    if get[find] == ']':
                        close.append(find)
                    elif get[find] == '[':
                        if len(close) > 1:
                            close.pop()
                        elif len(open) == 1:
                            ip = close.pop()
                            break
        ip += 1