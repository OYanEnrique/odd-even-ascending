# 🔢 Odd/Even Sorter

A command-line tool that takes exactly seven integer inputs, separates them into two lists based on whether they are odd or even, and then displays both lists sorted in ascending order.

## Features

* **Data Categorization**: Efficiently separates numbers into even and odd lists using a list of lists data structure.
* **Fixed Input**: Accepts exactly seven integer values from the user.
* **Ascending Order**: Both the final even and odd lists are sorted numerically from lowest to highest.
* **Concise Logic**: Uses a conditional expression (ternary operator) for clean and efficient appending of values.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `odd_even_ascending.py`).
3.  Run the script from your terminal:
    ```sh
    python odd_even_ascending.py
    ```
4.  The program will prompt you to enter seven numbers, one by one.
5.  After the seventh number is entered, the script will print the final sorted lists of even and odd numbers.

### Example Session

```sh
> python odd_even_ascending.py
------Odd or Even Ascending Order------
Enter a number:
4
Enter a number:
7
Enter a number:
2
Enter a number:
1
Enter a number:
9
Enter a number:
6
Enter a number:
5
The even values ​​entered were [2, 4, 6]
The odd values ​​entered were [1, 5, 7, 9]
