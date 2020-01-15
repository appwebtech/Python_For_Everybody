import re
text = open('regex_sum_301266.txt')

for line in text:
    line = line.strip()
    y = re.findall('([0-9]+)',line)

    if len(y) > 0:
        print(sum(map(int, y)))
