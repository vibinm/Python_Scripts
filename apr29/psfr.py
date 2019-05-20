fp = open('/etc/passwd')


for line_no, temp in enumerate(fp, 1):
    if 6 <= line_no <= 10:
        print('{:>6}  {}'.format(line_no, temp), end='')


fp.close()