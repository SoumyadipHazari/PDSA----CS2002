# Exception Handling in Python

An exception is Python’s way of stopping the program when it encounters a problem it cannot resolve.

## Types of common errors

- SyntaxError

Something structurally wrong in code

    if x > 3 print("hi")
    # SyntaxError: ivalid syntax

- NameError
  
Variable used before assignment.

    print(a)
    # NameError: name 'a' is not defined


- ZeroDivisonError
  
you can't divide anything by zero (0)

    print(a)
    # NameError: name 'a' is not defined

- IndexError

An IndexError means you tried to access an element at a position that doesn’t exist in the sequence.

    l = [1,2,3,4]
    print(l[6])
    ## IndexError: list index out of range

### Why do we need Exception Handling??
- Prevent crashes
- Use fallback values
- Retry Operations
- Skip bad inputs

### The try/except/else structure
    
    try:
        # Code that might throw an exception
    except SpecificError:
        # Code to run if that specific error occurs
    except (Error1, Error2):
        # Handle multiple errors together
    except:
        # Handle any other errors (general catch)
    else:
        # Runs only if try block had NO errors


- try block

you put code inside try that may fail.

    try:
        # code where error might happen

- except block

Catches the error and prevents the program from crashing

    except (NameError, KeyError):
    print("Name or key error occurred")

- else block
  
Runs only when the try block succeeds (no errors)

    else:
    #... ← Execute if try runs without errors


    try:
    nums = [10, 20, 30]
    i = int(input("Enter index: "))
    print(nums[i])           # may cause IndexError
    except IndexError:
        print("That index does not exist!")
    except ValueError:
        print("You must enter a number!")
    except:
        print("Unexpected error occurred")
    else:
        print("Successful access.")
