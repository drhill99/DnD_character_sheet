spell_slots = [
    #0,1,2,3,4,5,6,7,8,9
    [0,0, [0,0,0,0,0,0,0,0,0,0]], #0
    [3,4, [0,2,0,0,0,0,0,0,0,0]], #1
    [3,5, [0,3,0,0,0,0,0,0,0,0]], #2
    [4,6, [0,4,2,0,0,0,0,0,0,0]], #3
    [4,7, [0,4,3,0,0,0,0,0,0,0]], #4
    [4,9, [0,4,3,2,0,0,0,0,0,0]], #5
    [4,10,[0,4,3,3,0,0,0,0,0,0]], #6
    [4,11,[0,4,3,3,1,0,0,0,0,0]], #7
    [4,12,[0,4,3,3,2,0,0,0,0,0]], #8
    [4,14,[0,4,3,3,3,1,0,0,0,0]], #9
    [4,15,[0,4,3,3,3,2,0,0,0,0]], #10
    [5,16,[0,4,3,3,3,2,1,0,0,0]], #11
    [5,17,[0,4,3,3,3,2,1,0,0,0]], #12
    [5,18,[0,4,3,3,3,2,1,1,0,0]], #13
    [5,19,[0,4,3,3,3,2,1,1,0,0]], #14
    [5,20,[0,4,3,3,3,2,1,1,1,0]], #15
    [5,21,[0,4,3,3,3,2,1,1,1,0]], #16
    [5,22,[0,4,3,3,3,3,1,1,1,1]], #17
    [5,23,[0,4,3,3,3,3,1,1,1,1]], #18
    [5,24,[0,4,3,3,3,3,2,1,1,1]], #19
    [5,25,[0,4,3,3,3,3,2,2,1,1]]  #20
]
def display_spell_table(stats):
    spell_table = []
    header = ["lvl","cantrips","Prepared", "levels", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    spell_table.append(header)
    spell_counts = []
    for i, row in enumerate(spell_slots):
        if i == 0: continue
        row_by_lvl = []
        row_by_lvl.append(str(i))
        row_by_lvl.append(str(row[0]))
        row_by_lvl.append(str(row[1]))
        row_by_lvl.append("  ")
        for i, spell_count in enumerate(row[2]):
            if i == 0: continue
            if spell_count == 0:
                row_by_lvl.append('-')
            else:
                row_by_lvl.append(str(spell_count))
        spell_counts.append(row_by_lvl)
    header_widths = [len(item) + 2 for item in header]
    total_width = sum(header_widths)
        
    spell_table.append("".join("'" for _ in range(total_width)))

    spell_table.extend(spell_counts)
    format_string = "".join(f"{{:^{w}}}" for w in header_widths)

    for i, row in enumerate(spell_table):
        # print(row)
        if i == 1:
            print(row)
        else:
            print(format_string.format(*row))
        if i > stats['lvl']:
            break

def prepared_spells(stats):
    return spell_slots[int(stats['lvl'])][1]



