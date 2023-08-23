fh = open('c:/Users/mariok/OneDrive - Neumann János Egyetem/01 Projects/py4e/words.txt')
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())