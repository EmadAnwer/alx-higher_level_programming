#!/usr/bin/python3
with open('/dev/stdout', 'w') as f:
    f.write(''.join(map(chr, range(65, 91))) + '\n')
