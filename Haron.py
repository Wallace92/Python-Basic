# Wzor Harona umozliwa wyliczenie pierwiastka z dowolnej liczbu
S = 49

x = 1
for i in range(0, 9):
    x = (1.0 / 2.0) * (x + S / x)
    print(x)