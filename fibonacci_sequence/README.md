# Fibonacci Sequence Generator

## Description

Fibonacci sequence begins with 0 and 1, the next number is always the sum of the previous two numbers. This program is a Fibonacci sequence generator that allows the user to specify the number of terms they want to generate.

## How it Works

- The `main` function begins by first printing a welcome message and prompts the user to enter the number of terms they want to generate in the Fibonacci sequence.

- Inside a `while True` loop, the program attempts to convert the user input into an integer using `int(input())`. If the conversion fails due to a `ValueError`, it catches the exception and displays an error message. The loop continues until a valid integer greater than zero is entered.

- After obtaining the number of terms, the program checks if it exceeds a predefined maximum limit (`max_terms`). If it does, a warning message is displayed, indicating that generating more than the specified number of terms may take a long time. The user is prompted to press Enter to proceed.

- The program then calls the `generate_fibonacci_sequence` function, passing the `num_terms` as an argument. This function is responsible for generating the Fibonacci sequence.
    - Inside the `generate_fibonacci_sequence` function, the input `n` is first validated. If `n` is less than or equal to zero, an empty list is returned since there are no terms to generate. The sequence is initialized with the first two terms, [0, 1].
    - A `while` loop is used to generate the remaining terms of the Fibonacci sequence. It continues until the length of the sequence list reaches the desired number of terms `n`. In each iteration, the next term is calculated by adding the last two terms of the sequence (`sequence[-1]` and `sequence[-2]`), and the result is appended to the sequence list.
    - Once the sequence is generated, the `generate_fibonacci_sequence` function returns the sequence as a list.

- Back in the main function, the generated Fibonacci sequence is stored in the `sequence` variable. The program then prints a message indicating the number of terms in the sequence.

- Finally, a loop iterates through each term in the sequence list and prints it, separated by a space. The loop ensures that each term is printed on the same line. After printing the sequence, an extra newline is printed to improve the formatting.

## Program Input & Output
When you run `fibonacci_sequence.py`, the output will look like this;

```

Fibonacci Sequence Generator

Enter the number of terms to generate (1 or more):
> 0
Invalid input. Please enter a valid integer greater than zero.
Enter the number of terms to generate (1 or more):
> 1

The Fibonacci sequence up to 1 terms:
0 1 

sh-5.1$ /usr/bin/python3 ".../fibonacci_sequence/fibonacci_sequence.py"

Fibonacci Sequence Generator

Enter the number of terms to generate (1 or more):
> 20

The Fibonacci sequence up to 20 terms:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 

sh-5.1$ /usr/bin/python3 ".../fibonacci_sequence/fibonacci_sequence.py"

Fibonacci Sequence Generator

Enter the number of terms to generate (1 or more):
> 150
Warning: Generating more than 100 terms may take a long time.
Press Enter to begin...

The Fibonacci sequence up to 150 terms:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 12586269025 20365011074 32951280099 53316291173 86267571272 139583862445 225851433717 365435296162 591286729879 956722026041 1548008755920 2504730781961 4052739537881 6557470319842 10610209857723 17167680177565 27777890035288 44945570212853 72723460248141 117669030460994 190392490709135 308061521170129 498454011879264 806515533049393 1304969544928657 2111485077978050 3416454622906707 5527939700884757 8944394323791464 14472334024676221 23416728348467685 37889062373143906 61305790721611591 99194853094755497 160500643816367088 259695496911122585 420196140727489673 679891637638612258 1100087778366101931 1779979416004714189 2880067194370816120 4660046610375530309 7540113804746346429 12200160415121876738 19740274219868223167 31940434634990099905 51680708854858323072 83621143489848422977 135301852344706746049 218922995834555169026 354224848179261915075 573147844013817084101 927372692193078999176 1500520536206896083277 2427893228399975082453 3928413764606871165730 6356306993006846248183 10284720757613717413913 16641027750620563662096 26925748508234281076009 43566776258854844738105 70492524767089125814114 114059301025943970552219 184551825793033096366333 298611126818977066918552 483162952612010163284885 781774079430987230203437 1264937032042997393488322 2046711111473984623691759 3311648143516982017180081 5358359254990966640871840 8670007398507948658051921 14028366653498915298923761 22698374052006863956975682 36726740705505779255899443 59425114757512643212875125 96151855463018422468774568 155576970220531065681649693 251728825683549488150424261 407305795904080553832073954 659034621587630041982498215 1066340417491710595814572169 1725375039079340637797070384 2791715456571051233611642553 4517090495650391871408712937 7308805952221443105020355490 11825896447871834976429068427 19134702400093278081449423917 30960598847965113057878492344 50095301248058391139327916261 81055900096023504197206408605 131151201344081895336534324866 212207101440105399533740733471 343358302784187294870275058337 555565404224292694404015791808 898923707008479989274290850145 1454489111232772683678306641953 2353412818241252672952597492098 3807901929474025356630904134051 6161314747715278029583501626149 

```
