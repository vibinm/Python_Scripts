import sys

if len(sys.argv) != 3:
    print('Usage:', file=sys.stderr)
    print('{} src-file dest-file'.format(sys.argv[0]), file=sys.stderr)

with open(sys.argv[1]) as fp, open(sys.argv[2], 'w') as fw:
    fw.write(fp.read())
