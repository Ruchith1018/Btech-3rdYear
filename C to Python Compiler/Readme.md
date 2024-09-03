
# C to Python Compiler using Lex and Yacc

This project implements a simple compiler that translates C code into Python code. The compiler is built using Lex and Yacc, which are tools commonly used for lexical analysis and parsing in compiler design.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Compilers are programs that translate code written in one programming language into another. This project focuses on translating C code into Python code using Lex for lexical analysis and Yacc for syntax parsing. The goal is to demonstrate the process of creating a basic compiler.

## Features

- **Lexical Analysis:** Using Lex to tokenize C code.
- **Syntax Parsing:** Using Yacc to parse the tokenized code and generate corresponding Python code.
- **Translation:** Basic translation of C constructs (e.g., loops, conditionals, function definitions) into Python.

## Technologies Used

- C Programming Language
- Lex (Flex)
- Yacc (Bison)
- Python

## Usage

1. Write the C code you want to translate.
2. Run the Lex and Yacc tools to compile the translator.
3. Use the compiled program to convert the C code into Python.

## Example

Given a simple C program:

```c
#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int sum = a + b;
    printf("Sum: %d\n", sum);
    return 0;
}
```
The compiler will translate it to:

```python
a = 5
b = 10
sum = a + b
print("Sum:", sum)
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## Acknowledgements
This project is inspired by compiler design courses and tutorials on using Lex and Yacc.
Special thanks to the developers of Flex and Bison, and the open-source community.
