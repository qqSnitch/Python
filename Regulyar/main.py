# import re
# a=input()
# x=re.findall(r'^[A-Za-z]+',a)
# print(x)

# import re
# a=input()
# x=re.findall(r'[A-Za-z]+$',a)
# print(x)

# import re
# a=input()
# x=re.findall(r'\bкот',a)
# print(x)

import re
a=input()
x=re.findall(r'кот{2,}',a)
print(x)