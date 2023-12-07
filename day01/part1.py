total = 0
with open('input.txt') as inp:
    for line in inp:
        ans = ''
        for start in line:
            if start.isdigit():
                ans += start
                break
        
        for start in line[::-1]:
            if start.isdigit():
                ans += start
                break

        total += int(ans)

print(total)