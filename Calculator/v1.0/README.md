# Calculator

## version 1.0

A basic Calculator with basic arithmetic functions and access to previous result.

## Functionalities

1. Expression Solving: Takes an expression as input and returns is value as result.
	Can perform:
		- Addition
		- Subtraction
		- Multiplication
		- Division
	
	Handles:
		- Brackets in expression
2. Access to previous result: Can use result from the previous expression in the new expression as 'ans'.

## Implementation

- A `prompt()` function is used to create the user interface.
	- It clears the command line interface using the os module.
	- Then prints the instructions to the user based on some booleans.

- To solve the expression a series of functions is used following the BODMAS order
	- First the expression is split into a list of operands, operators and brackets called `op_stack` and sent to a function called `solve()` which is an aggregation of multiple handling functions.

	- Then a recursive function called `bracket_process()` is used to solve expressions inside brackets and simplify the parent expression by replacing the bracketed part with its result.
		- It checks for a '(' character in the op_stack and iterates until the count of '(' is same as count of ')'. i.e. the original bracket is getting closed.
		- Then it takes the expression between those 2 brackets and solves it in another `solve()` function.
		- The portion of the list from the opening to closing bracket is replaced with the return value from the recursive function called.
	
	- Then the `muldiv()` function is called to handle the multiplication and division operations as they take more priority.
	- Followed by the `addsub()` function to completely solve the expression and reduce the `op_stack` into just one number.
	- These 2 functions work by adding operands or operators from `op_stack` to a new stack and if it finds an operator that it is supposed to handle, like `/` for `muldiv()` function, then it takes the top element from the new stack and the next element from the `op_stack`, performs  the operation and replaces the top element of the new stack with the result.

- The final result from the `op_stack` is saved in the variable `ans` and displayed.

- This way the variable `ans` can be used in the next operation. If there is a substring 'ans' in the expression string, it is replaced by the string typecast of `ans`'s value.

- Exception Handling:
	- It is checked at the beginning if the expression contains any non-numeric character or operator/bracket which is not implemented.
	- If the expression is invalid, the op_stack will not reduce to just one number.