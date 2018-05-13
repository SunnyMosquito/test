from os import path
import time
import re

d = path.dirname(__file__)

rp = path.join(d, 'simple.txt')
wp = path.join(d, 'results.txt')
# p = path.join(d, '斗破苍穹.txt')

pattern = re.compile('(^第.*章.*)')

start = time.time()
with open(rp) as rf, open(wp,'a+') as wf:
    for line in rf:
        m = re.match(pattern, line)
        if m is not None:
            # print(m.group())
            # print(m.groups())
        else:
            # print('m is none')
            pass
end = time.time()
print(end - start)

