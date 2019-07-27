# CSV Spreadsheet Fixer

### Usage
```
python fixchart.py <filename> [-a -r]
```
-a: Add Address 2 column

-r: Remove rows with the same Last Name + Address

Note: you can use multiple flags at the same time to do multiple operations, but I would suggest doing one at a time and making sure the operation completed successfully, just in case.

### Notes
This program assumes the spreadsheet has the following format:

*** | Address | Address 2 | *** | First | First 2 | Mid | Mid 2 | Last | *** | ...
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 

##### For the -a flag:

This program assumes the spreadsheet is in alphabetical order by address.

This program assumes that no more than two people with the same last name have the same address.
