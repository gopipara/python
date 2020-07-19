The idea is to print digits starting from 1-9 to 9-1 in the increasing followed by decreasing sequence through squaring number of ones, i.e. if arg passed to this script is 4; `1111*1111`, if arg passed is 6; `111111*111111`.

**Note:** Script by default produces output for an arg 9 if no arg is passed or an arg above 9 is passed.

**Examples:**
1. arg passed is `4`
- `python squares_of_ones.py 4`
```
1
121
12321
1234321
```

2. arg passed is `6`
- `python squares_of_ones.py 6`
```
1
121
12321
1234321
123454321
12345654321
```
3. No arg passed
- `python squares_of_ones.py`
```
1
121
12321
1234321
123454321
12345654321
1234567654321
123456787654321
12345678987654321
```
4. Arg above 9 is passed
- `python squares_of_ones.py 11`
```
1
121
12321
1234321
123454321
12345654321
1234567654321
123456787654321
```
