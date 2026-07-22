for i in range(3):
    try:
        s = input()
    except EOFError:
        print('EOF')
        break
    print(repr(s))
