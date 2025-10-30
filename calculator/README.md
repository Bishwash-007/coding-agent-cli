# Calculator App

This is a simple command-line calculator application written in Python. It evaluates arithmetic expressions and outputs the result in JSON format.

## Features

*   Supports basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).
*   Handles operator precedence.
*   Outputs results in a structured JSON format.

## Usage

To run the calculator, execute the `main.py` script with your desired arithmetic expression as a command-line argument.

```bash
python main.py "3 + 5"
```

Example:

```bash
python main.py "10 / 2 + 3 * 4"
```

The output will be a JSON string:

```json
{
  "expression": "10 / 2 + 3 * 4",
  "result": 17
}
```

If no expression is provided, it will display a usage message:

```bash
python main.py
```

## Files

*   `main.py`: The entry point of the application. It parses command-line arguments, calls the calculator, and formats the output.
*   `pkg/calculator.py`: Contains the `Calculator` class responsible for evaluating arithmetic expressions.
*   `pkg/render.py`: Contains the `format_json_output` function, which formats the expression and result into a JSON string.