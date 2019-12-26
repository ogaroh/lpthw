formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('One', 'Two', 'Three', 'Four'))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter.format('A', 'B', 'C', 'Ogaro')))
print(formatter.format(
    "Roses are red,",
    "Violets are blue,",
    "I stay up in bed,",
    "Just thinking 'bout you."
))