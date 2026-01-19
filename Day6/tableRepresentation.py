import prettytable

table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name","Type"]
table.add_row(["Charmander","Fire"])
table.add_row(["Squirtle","Water"])
table.add_row(["Bulbasaur","Grass/Poison"])
table.add_row(["Pikachu","Electric"])
table.align = "l"
print(table)