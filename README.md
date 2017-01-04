# ascii-tables

Create a pretty looking ascii table.

## Usage:
```
python convert.py input_file.txt
```

Where `input_file.txt` contains your input seperated by tabs and new-line characters and the output table is printed on the terminal.

## Example:
### Input:
```
Col 1	Col 2	Col 3	Col 4
Val1	Val2	Val3	Val4
Val11	Val22	Val33	Val44
Vala	Valb	Valc	Vald
```
### Output:
```
+-------+-------+-------+-------+
| Col 1 | Col 2 | Col 3 | Col 4 |
+-------+-------+-------+-------+
| Val1  | Val2  | Val3  | Val4  |
+-------+-------+-------+-------+
| Val11 | Val22 | Val33 | Val44 |
+-------+-------+-------+-------+
| Vala  | Valb  | Valc  | Vald  |
+-------+-------+-------+-------+
```
