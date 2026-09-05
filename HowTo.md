# <div align="center">RegexIt</div>
## How to download and use RegexIt
### Installation (Python 3.X required)
First download `RegexIt.py` from /RequestTimeout/RegexIt/src/RegexIt.py

Then place the Python file somewhere accessible, for example:
```text
C:\RegexIt\RegexIt.py
```

Then, whenever you want to test some regex, open a terminal and run:
```bash
python "C:\RegexIt\RegexIt.py"
```
and RegexIt will open a window.
### Using RegexIt
Enter your regular expression into the **Regex Pattern** box.

Then enter or paste the text you want to test the regular expression against into the **Test String** box.

RegexIt will automatically search the text and display the matches in the **Result** box.

For example:
```text
Regex Pattern:
\d+

Test String:
I have 12 apples and 345 bananas.

Result:
12, 345
```
### Requirements
* Python 3.x
* PyQt5
