TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    new_line = '||'
    line_end = ""
    
    if tile == new_line:
        print('\n')
    else:
        print(tile, end=line_end)