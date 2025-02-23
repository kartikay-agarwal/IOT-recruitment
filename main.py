def identify_language():
    N = int(input())
    
    tcount = 0
    scount = 0
    
    for _ in range(N):
        line = input()

        tcount += line.count('t') + line.count('T')
        scount += line.count('s') + line.count('S')
    
    if tcount > scount:
        return "English"
    else:
        return "French"

print(identify_language())
