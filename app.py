from multiplo import ispositive, multiplo

while True:
    try:
        n = input("""\nEnter a natural number (i.e. integer and greater than 0)
or Q to quit: """)

        if n == 'q' or n == 'Q':
            break
        n = int(n)
        if not ispositive(n):
            raise ValueError
        m = ''
        if multiplo(5, n):
            m += 'fizz'
        if multiplo(7, n):
            m += 'buzz'
        if m == '':
            m += 'miss'
        print()
        print(m)
        print()

    except ValueError:
        print("\nPlease enter a valid natural number (integer and greater than 0).")
