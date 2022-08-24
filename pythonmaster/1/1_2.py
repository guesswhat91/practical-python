print(3 + 4*5)
print(23.45 / .01)
print(7 / 4)
print(7 // 4)
x = 1172.5
print(x.as_integer_ratio())
print(x.is_integer())
y = 12345
print(y.numerator)
print(y.denominator)
print(y.bit_length)

symbols = 'AAPL IBM MSFT YHOO SCO'
print(symbols[0])
print(symbols[1])
print(symbols[2])
print(symbols[-1])
print(symbols[-2])
print(symbols[:4])
print(symbols[-4:])
print(symbols[5:8])

symbols += ' GOOG'
print(symbols)
symbols = 'HPQ ' + symbols
print(symbols)
symlist = symbols.split()
print(symlist)

for s in symlist:
    print('s =', s)