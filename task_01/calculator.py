
def calculate(expression):

    expression = expression.replace(' ', '')

    allowed_chars = set('0123456789+-*/().')
    if not all(char in allowed_chars for char in expression):
        raise ValueError("Invalid characters in expression. Only numbers and +, -, *, /, (, ) are allowed.")

    if not expression:
        raise ValueError("Empty expression")
    
    try:

        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")

def main():
    print("Type 'quit' or 'exit' to leave\n")
    
    while True:
        try:
            user_input = input(">>> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye! 👋")
                break

            if not user_input:
                continue

            result = calculate(user_input)
            

            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            print(f"Result: {result}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()