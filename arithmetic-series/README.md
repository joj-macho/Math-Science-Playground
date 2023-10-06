# Arithmetic Series Generator

## Description

An arithmetic series is the sum of the terms of an arithmetic sequence. An arithmetic sequence is a sequence of numbers in which the difference of any two successive members is a constant. This constant difference is known as the "common difference."

An arithmetic sequence is defined by the first term ($a_1$​), the common difference ($d$), and the term number ($n$). The nth term of an arithmetic sequence is given by:
$$a_n = a_1 + (n-1)d$$

The sum of the first $n$ terms of an arithmetic sequence (i.e., an arithmetic series) is calculated using the following formula:
$$S_n = \frac{n}{2} \times (a_1 + a_n)$$
where $S_n$ is the sum of the first $n$ terms of the series, $a_1$ is the first term of the series, $a_n$ is the nth term of the series, $n$ is the number of terms in the series.

This program, Arithmetic Series Generator, allows users to generate an arithmetic series and calculate the sum of the series given the first term, common difference, and the number of terms. An arithmetic series is the sum of the terms of an arithmetic sequence.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly prompt the user for input: the first term, common difference, and the number of terms.

- The `generate_arithmetic_series` function generates the arithmetic series based on the input provided by the user. It utilizes a list comprehension to create a list of terms by adding the common difference to the previous term, starting with the first term.

- The `arithmetic_series_sum` function calculates the sum of the arithmetic series using the arithmetic series sum formula. It calculates the last term of the series using the given first term, common difference, and number of terms. Then it uses the sum formula, which is given by $S_n$ above, i.e. `(number of terms / 2) * (first term + last term)`, to calculate the sum.

- After obtaining the necessary input and generating the arithmetic series and its sum, the program displays the generated series and the sum of the series.

- The user can repeat the process by entering new values for the first term, common difference, and the number of terms, or exit the program.

## Program Input & Output

When you run the program, `arithmetic_series.py`, the output will look like this;

```
Arithmetic Series Sum

Enter the first term: 5
Enter the common difference: 3
Enter the number of terms: 10
Arithmetic Series for 10 terms: a_1 = 5.0, d = 3.0
[5.0, 8.0, 11.0, 14.0, 17.0, 20.0, 23.0, 26.0, 29.0, 32.0]

The sum of the arithmetic series is: 185.0

.
.
.

Enter the first term: 42
Enter the common difference: 11
Enter the number of terms: 5
Arithmetic Series for 5 terms: a_1 = 42.0, d = 11.0
[42.0, 53.0, 64.0, 75.0, 86.0]

The sum of the arithmetic series is: 320.0
```