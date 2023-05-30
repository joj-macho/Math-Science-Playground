# Multiplication Table

## Description

This program is a simple multiplication table generator. It prompts the user to enter the size of the table and prints a multiplication table of the given size, displaying the multiplication values in a formatted and aligned manner.


## How it Works

- The `main` function is defined, tt first calls the `get_table_size` function to get the size of the multiplication table from the user.

- The `get_table_size` function prompts the user to enter the size of the multiplication table. It validates the input and ensures that a positive integer greater than or equal to 1 is provided. If the input is valid, the function returns the size.

- Once the size is obtained, the `main` function calls the `print_multiplication_table` function with the obtained size as an argument. The `print_multiplication_table` function takes the size as input and prints a multiplication table of the given size. It first prints the table header, including the size of the table. Then it generates the horizontal number labels using a loop. Next, it iterates through each row and column to calculate and print the multiplication values. The numbers are formatted using f-strings to ensure proper alignment.

- If an exception occurs during the execution of the program, such as an invalid input or any other error, it is caught by the `try-except` block in the `main` function. The error message is printed to the console, providing information about the encountered exception.


## Program Output

When you run the program `multiplication_table.py`, the output will look like this;

```

Enter the size of the multiplication table:
> 6

 6x6 Multiplication Table.

  |   0   1   2   3   4   5   6
--+---------------------
 0|   0   0   0   0   0   0   0
 1|   0   1   2   3   4   5   6
 2|   0   2   4   6   8  10  12
 3|   0   3   6   9  12  15  18
 4|   0   4   8  12  16  20  24
 5|   0   5  10  15  20  25  30
 6|   0   6  12  18  24  30  36

sh-5.1$ /usr/bin/python3 ".../multiplication-table/multiplication_table.py"

Enter the size of the multiplication table:
> 12

 12x12 Multiplication Table.

  |   0   1   2   3   4   5   6   7   8   9  10  11  12
--+---------------------------------------
 0|   0   0   0   0   0   0   0   0   0   0   0   0   0
 1|   0   1   2   3   4   5   6   7   8   9  10  11  12
 2|   0   2   4   6   8  10  12  14  16  18  20  22  24
 3|   0   3   6   9  12  15  18  21  24  27  30  33  36
 4|   0   4   8  12  16  20  24  28  32  36  40  44  48
 5|   0   5  10  15  20  25  30  35  40  45  50  55  60
 6|   0   6  12  18  24  30  36  42  48  54  60  66  72
 7|   0   7  14  21  28  35  42  49  56  63  70  77  84
 8|   0   8  16  24  32  40  48  56  64  72  80  88  96
 9|   0   9  18  27  36  45  54  63  72  81  90  99 108
10|   0  10  20  30  40  50  60  70  80  90 100 110 120
11|   0  11  22  33  44  55  66  77  88  99 110 121 132
12|   0  12  24  36  48  60  72  84  96 108 120 132 144

sh-5.1$ /usr/bin/python3 ".../multiplication-table/multiplication_table.py"

Enter the size of the multiplication table:
> 18

 18x18 Multiplication Table.

  |   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
--+---------------------------------------------------------
 0|   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
 1|   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
 2|   0   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  32  34  36
 3|   0   3   6   9  12  15  18  21  24  27  30  33  36  39  42  45  48  51  54
 4|   0   4   8  12  16  20  24  28  32  36  40  44  48  52  56  60  64  68  72
 5|   0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90
 6|   0   6  12  18  24  30  36  42  48  54  60  66  72  78  84  90  96 102 108
 7|   0   7  14  21  28  35  42  49  56  63  70  77  84  91  98 105 112 119 126
 8|   0   8  16  24  32  40  48  56  64  72  80  88  96 104 112 120 128 136 144
 9|   0   9  18  27  36  45  54  63  72  81  90  99 108 117 126 135 144 153 162
10|   0  10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170 180
11|   0  11  22  33  44  55  66  77  88  99 110 121 132 143 154 165 176 187 198
12|   0  12  24  36  48  60  72  84  96 108 120 132 144 156 168 180 192 204 216
13|   0  13  26  39  52  65  78  91 104 117 130 143 156 169 182 195 208 221 234
14|   0  14  28  42  56  70  84  98 112 126 140 154 168 182 196 210 224 238 252
15|   0  15  30  45  60  75  90 105 120 135 150 165 180 195 210 225 240 255 270
16|   0  16  32  48  64  80  96 112 128 144 160 176 192 208 224 240 256 272 288
17|   0  17  34  51  68  85 102 119 136 153 170 187 204 221 238 255 272 289 306
18|   0  18  36  54  72  90 108 126 144 162 180 198 216 234 252 270 288 306 324
```

