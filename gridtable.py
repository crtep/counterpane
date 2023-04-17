## Copyright 2023, Carter Teplica

## Copying and distribution of this file, with or without modification, are permitted in any medium 
## without royalty, provided the copyright notice and this notice are preserved. This file is offered
## as-is, without any warranty.

import re
strip_ANSI_pat = re.compile(r"""
    \x1b     # literal ESC
    \[       # literal [
    [;\d]*   # zero or more digits or semicolons
    [A-Za-z] # a letter
    """, re.VERBOSE).sub

def strip_ANSI(s):
    return strip_ANSI_pat("", s)

def table(data, row_labels=None, col_labels=None, key=None, unicode=True, spaces=True):
    """
    Given a grid of short multiline strings, assemble it into a 2D text-based table.
    
    Usage:
    
    >>> from gridtable import table
    >>> print(table([["cat", "horse", "least\nweasel"], ["blue-\ntongued\nskink", "T. rex", "dog"]]))
    
         cat │  horse │  least 
             │        │ weasel 
    ─────────┼────────┼────────
       blue- │ T. rex │    dog 
     tongued │        │        
       skink │        │        

    data:       data in the table body
    row_labels: labels for the rows
    col_labels: labels for the columns
    key:        contents of the upper-left corner cell, if there are row and column labels
    unicode:    use the unicode box-drawing characters ─┼│ instead of -+|
    spaces:     put a margin of one space to the left and right of text
    """

    if row_labels is not None and col_labels is not None:
        if key is None:
            key = ""
        col_labels = [key] + col_labels

    if col_labels is not None:
        data = [col_labels] + data
    
    if row_labels is not None:
        for i in range(len(row_labels)):
            data[i + int(col_labels is not None)] = [row_labels[i]] + data[i + int(col_labels is not None)]
    
    if unicode:
        vertical_sep, horizontal_sep, cross = "\u2502\u2500\u253c"
    else:
        vertical_sep, horizontal_sep, cross = "|-+"

    output = ""
    
    data = [[cell.split("\n") for cell in row] for row in data]
    widths = [max(len(strip_ANSI(line)) for row in data for line in row[j]) for j in range(len(data[0]))]

    margin = " "*spaces

    for i in range(len(data)):

        n_subrows = max(len(cell) for cell in data[i])

        row = data[i]

        for s in range(n_subrows):
            line = ""
            for j in range(len(row)):
                cell = row[j]
                print_data = " " * widths[j]
                if len(cell) > s:
                    print_data = print_data[0:-len(strip_ANSI(cell[s]))] + cell[s]
                line += " " + print_data + " "
                if j < len(row) - 1:
                    line += vertical_sep
                else:
                    line += "\n"

            output += line

        if i < len(data) - 1:
            output += cross.join([horizontal_sep * (w + 2*len(margin)) for w in widths]) + "\n"
    
    return output