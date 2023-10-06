# Geometric Series

## Description

A geometric series is the sum of the terms of a geometric sequence. A geometric sequence is a sequence of numbers in which each term after the first is found by multiplying the previous one by a fixed, non-zero number called the "common ratio."

In a geometric sequence, the nth term ($a_n$) is given by:
$$a_n = a_1 \times r^{n-1}$$
where $a_1$ is the first term, $r$ is the common ratio, and $n$ is the term number.

The sum of the first $n$ terms of a geometric sequence (i.e., a geometric series) is calculated using the following formula:
$$S_n = \frac{a_1 \times (1 - r^n)}{1-r}$$
where $S_n$ is the sum of the first $n$ terms of the series, $a_1$ is the first term of the series, $r$ is the common ratio, and $n$ is the number of terms in the series.

## How it Works

- The program starts with a `main` function. Inside this function, a while loop is used to repeatedly prompt the user for input: the first term, common ratio, and the number of terms.

- The `generate_geometric_series` function generates the geometric series based on the input provided by the user. It utilizes a list comprehension to create a list of terms by multiplying the previous term by the common ratio.

- The `geometric_series_sum` function calculates the sum of the geometric series using the geometric series sum formula. If the common ratio is 1, it uses a simplified formula, otherwise, it uses the general formula. The sum is calculated using the formula provided above.

- After obtaining the necessary input and generating the geometric series and its sum, the program displays the generated series and the sum of the series.

- The user can repeat the process by entering new values for the first term, common ratio, and the number of terms, or exit the program.

## Program Input & Output

When you run the program, `geometric_series.py`, the output will look like this;

```

Welcome to the Geometric Series Generator

Enter the first term: 1
Enter the common ratio: 2
Enter the number of terms: 10

The generated geometric series is:
[1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0]

The sum of the geometric series is: 1023.0

.
.
.

Enter the first term: 10
Enter the common ratio: 5
Enter the number of terms: 10

The generated geometric series is:
[10.0, 50.0, 250.0, 1250.0, 6250.0, 31250.0, 156250.0, 781250.0, 3906250.0, 19531250.0]

The sum of the geometric series is: 24414060.0
```