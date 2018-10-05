def add_yes(word):
    return word + ', yes!'


print(dir())
# [..., 'add_yes']

from wordifier import *

print('add_yes' in dir())
word = "central"
print(verb(word))

"""
出力結果
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add_yes']
True
centralize
"""
