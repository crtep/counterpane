# counterpane

Given a grid of short multiline strings, assemble it into a 2D text-based table.
    
Usage:

```python
>>> from counterpane import table
>>> table([["cat", "horse", "least\nweasel"], ["blue-\ntongued\nskink", "T. rex", "dog"]])

"""
     cat │  horse │  least 
         │        │ weasel 
─────────┼────────┼────────
   blue- │ T. rex │    dog 
 tongued │        │        
   skink │        │        
"""
```

    data:       data in the table body
    row_labels: labels for the rows
    col_labels: labels for the columns
    key:        contents of the upper-left corner cell, if there are row and column labels
    unicode:    use the unicode box-drawing characters ─┼│ instead of -+|
    spaces:     put a margin of one space to the left and right of text
