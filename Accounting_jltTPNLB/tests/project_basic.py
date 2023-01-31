import re


def string_amount_separator(entry):
    items = list()
    for i in entry:
        match = re.match(r"([A-Z a-z]+) ([0-9]+)", i)
        if match:
            items.append(match.groups())
    return items


def prettier(entry_group):
    dr_entry = entry_group[0][0]
    dr_amount = entry_group[0][1]
    cr_entry = entry_group[1][0]
    cr_amount = entry_group[1][1]
    spacing = " "*5
    cr_spacing = " "*15
    print("--------------------------------------------------------------------------------")
    print(f" {dr_entry} dr {spacing} {dr_amount}")
    print(f"{cr_entry} cr {cr_spacing} {cr_amount}")
    print("--------------------------------------------------------------------------------")


entries = input("Enter the entry entry1 dr entry2 cr\n").split('|')
value = string_amount_separator(entries)
prettier(value)
