

# Niny
**Stack-oriented programming language, with Python under the hood**

***Still in developing***

Niny - stack-oriented programming language, powered with Python, but in future, it will be also compilable
Extension *".nn"*

# Examples
*Hello world*

    push "Hello world!\n"
    dump

*Factorial*

    macro loop do
	    dup
	    push -1
	    add
	    fact
	    mult
	end

	macro fact do
	    dup
	    dup

	    push 0
	    =

	    swp
	    push 1
	    =

	    or
	    not
	    if do loop
	end

*Program that takes last number from stack, and if it is greater than zero, increases it by one, otherwise, decreases it by one*

    macro y do
	    push 1
	    add
	end

	macro n do
	    push 1
	    swp
	    sub
	end

	if do y else do n

*Program that takes last number from stack, and prints sum of all numbers from that number to 1*

    macro y do
	    swp
	    get 0
	    add
	    swp
	    push -1
	    add
	    loop
	end

	macro loop do
	    dup
	    push 1
	    =
	    not
	    if do y
	end

	macro sum do
	    push 0
	    swp
	    loop
	    add
	end

	sum
	dump "\n"

*Program that takes last number from stack and prints all numbers from that number to 1*

    macro y do
	    push -1
	    add
	    nums
	end

	macro nums do
	    dump "\n"
	    dup
	    push 1

	    =
	    not

	    if do y
	end

	nums

*Basic program to concatenate two strings from stack*

    push "Fizz"
	push "Buzz"

	swp $ If you remove this line, you will get "BuzzFizz" instead of "FizzBuzz", note this
	add

*Basic program to add two nums from stack*

    push 2
    push 3
	
	add
# Docs

 - Use **"$"** sign for **commenting**.
 - Command **"push"** for **adding an element to the end of stack**, **requires 1 argument**.

   *Example:*

       $ stack = []
       push 5 $ stack = [5]
       push 4 $ stack = [5, 4]

- Command **"del"** for **deleting a macro**, **requires 1 argument**.

  *Example:*

      macro foo do
          push "foo"
          dump "\n"
          pop
      end

        foo $ OUT:  "foo"
        del foo
      foo 
      $ OUT: 
      $ Unknown command
      $ Line 9
      $  -> foo

- Command **"add"** for **arithmetic sum** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "add" removes the elements being operated on.*

  *Example:*

      $ stack = []
      push 3 $ stack = [3]
      push 5 $ stack = [3, 5]
      push 6 $ stack = [3, 5, 6]
      add $ stack = [3, 11]

- Command **"sub"** for **arithmetic subtraction** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "sub" removes the elements being operated on.*

  *Example:*

      push 3 $ stack = [3]
      push 6 $ stack = [3, 6]
      push 5 $ stack = [3, 6, 5]
      swp $ stack = [3, 5, 6]
      $ If you remove "swp" you will get -1 instead of 1, note this
      sub $ stack = [3, 1]

- Command **"mult"** for **arithmetic multiplication** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "mult" removes the elements beign operated on.*

  *Example:*

      push 3 $ stack = [3]
      push 6 $ stack = [3, 6]
      push 5 $ stack = [3, 6, 5]
      mult $ stack = [3, 30]

- Command **"pow"** for **arithmetic exponentiation** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "pow" removes the elements beign operated on.*

  *Example:*

      push 3 $ stack = [3]
      push 2 $ stack = [3, 2]
      push 3 $ stack = [3, 2, 3]
      pow $ stack = [3, 9]


- Command **"root"** for **taking root** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "root" removes the elements beign operated on.*

  *Example:*

        push 3 $ stack = [3]
      push 2 $ stack = [3, 2]
      push 4 $ stack = [3, 2, 4]
      root $ stack = [3, 2.0]

- Command **"div"** for **arithmetic division** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "div" removes the elements beign operated on.*

  *Example:*

      push 3 $ stack = [3]
      push 2 $ stack = [3, 2]
      push 6 $ stack = [3, 2, 6]
      div $ stack = [3, 3.0]

- Command **"type"** for **getting type** of last element in stack, **appends the result to end of the stack**, **requires at least 1 element in stack**.

  *Note: "type" removes the elements beign operated on.*

  *Note: the output has string type*

  *Example:*

      push 3 $ stack = [3]
      type $ stack = ["int"]

- Command **"or"** for **logic or** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "or" removes the elements beign operated on.*

  *Note: the output is 1 (true) or 0 (false)

  *Example:*

      push 1 $ stack = [1]
      push 0 $ stack = [1, 0]
      or $ stack = [1]


- Command **"not"** for **logic not** of last element in stack, **appends the result to end of the stack**, **requires at least 1 elements in stack**. 

  *Note: "not" removes the elements beign operated on.*

  *Note: the output is 1 (true) or 0 (false)

  *Example:*

      push 1 $ stack = [1]
      push 0 $ stack = [1, 0]
      not $ stack = [1, 1]

- Command **"and"** for **logic and** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "and" removes the elements beign operated on.*

  *Note: the output is 1 (true) or 0 (false)

  *Example:*

      push 1 $ stack = [1]
      push 0 $ stack = [1, 0]
      and $ stack = [0]

- Command **"=="** for **logic comparison** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "==" removes the elements beign operated on.*

  *Note: the output is 1 (true) or 0 (false)

  *Example:*

      push 1 $ stack = [1]
      push 0 $ stack = [1, 0]
      == $ stack = [0]

- Command **"<"** for **logic less than** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "<" removes the elements beign operated on.*

  *Note: the output is 1 (true) or 0 (false)

  *Example:*

      push 6 $ stack = [6]
      push 5 $ stack = [6, 5]
      < $ stack = [1]

- Command **">"** for **logic greater than** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: ">" removes the elements beign operated on.*

  *Note: the output is 1 (true) or 0 (false)

  *Example:*

      push 6 $ stack = [6]
      push 5 $ stack = [6, 5]
      > $ stack = [0]

- Command **"pop"** for **removing** last element in stack, **requires at least 1 elements in stack**. 

  *Example:*

      push 5 $ stack = [5]
      push 3 $ stack = [5, 3]
      pop $ stack = [5]

- Command **"dup"** for **duplicating** last element in stack, **requires at least 1 elements in stack**. 

  *Example:*

      push 5 $ stack = [5]
      push 3 $ stack = [5, 3]
      dup $ stack = [5, 3, 3]

- Command **"divmod"** **returns the quotient-remainder of the argument division** of two last elements in stack, **appends the result to end of the stack**, **requires at least 2 elements in stack**. 

  *Note: "dimod" removes the elements beign operated on.*

  *Example:*

      push 3 $ stack = [3]
      push 2 $ stack = [3, 2]
      push 6 $ stack = [3, 2, 6]
      divmod $ stack = [3, 3, 0]

- Command **"dump"** for **printing** last element in stack, **takes 1 optional argument, as a string**, **requires at least 1 elements in stack**. 

  **Known bug: you cant provide a string, with a space inside**

  *Example 1:*

      push 5
      dump
      $ OUT:
      $ ~./niny.py test.nn 
        $ 5~

     *Example 2:*

      push 5
      dump "\n"
      $ OUT:
      $ ~./niny.py test.nn
      $ 5
      $ ~

- Command **"inp"** for **taking user input**, **appends the result to end of the stack**.
- Command **"full"** for **printing full stack**.

  *Note: prints "[]" if stack is empty*.

  *Example:*

      push 1
      push 2
      push 3
      full
      $ OUT:
      $ 1
      $ 2
      $ 3

- Command **"swp"** for **changing places of last 2 elements**, **requires at least 2 elements in stack**.

  *Example:*

      push 1 $ stack = [1]
      push 2 $ stack = [1, 2]
      swp $ stack = [2, 1]

- Command **"get"** for **getting item in a stack by it's index**, **takes 1 optional argument, as int**

*Note: default index is **-1***

  *Example:*

      push 1 $ stack = [1]
      push 2 $ stack = [1, 2]
      push 3 $ stack = [1, 2, 3]
      get $ stack = [1, 2, 3, 3]
      get 1 $ stack = [1, 2, 3, 3, 2]
      get 2 $ stack = [1, 2, 3, 3, 2, 3]

- Command **"if"** for **conditions**, has 2 structures: **"if do macro_name_true"** or **"if do macro_name_true else do macro_name_false"**.

  *Note: macro_name_true or macro_name_false can be defined before or after the condition, as long as they are defined when the program passes to the condition*

  *Note: condition removes the elements beign checked on.*

  *Example:*

      macro equals do
        push "EQUALS"
        dump "\n"
        pop
        end

      macro other do
        push "OTHER"
        dump "\n"
        pop
      end

      push 5 $ stack = [5]
      push 6 $ stack = [5, 6]
      == $ stack = [0]
      if do equals else do other
      $ OUT:
      $ OTHER

- Command **"macro"** for **functions**, has static structure:

      macro macro_name do
      end
    All command inside the macro will be computed once you call the macro


        macro_name

    *Example:*


        macro hello_world do
          push "Hello World!"
          dump "\n"
          pop
      end

      hello_world
      $ OUT:
      $ Hello World!

  *Note: indentaion inside the macro isn't required*

  **Known bugs: you can't define a macro inside a macro**
