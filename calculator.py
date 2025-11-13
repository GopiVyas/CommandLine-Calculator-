# smart_calculator.py
import math

print("===== Advanced Command-Line Calculator =====")
print("Type 'exit' to quit | Type 'help' to see supported features\n")

#array is used to store last answer
last_answer = 0
history = []

def calculate(expression):
    """Safely evaluate a math expression with extra functions."""
    global last_answer
    try:
       # to show last answer when user types 'ans'
        expression = expression.replace("ans", str(last_answer))

      
        expression = expression.replace("^", "**")

        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names["abs"] = abs  # allow abs()

        result = eval(expression, {"__builtins__": None}, allowed_names)
        last_answer = result
        return result
    except Exception:
        return "❌ Invalid expression!"

while True:
    user_input = input("Enter expression ➤ ")

    # Exit condition
    if user_input.lower() == "exit":
        print("\nCalculation History:")
        for i, h in enumerate(history, 1):
            print(f"{i}) {h}")
        print("Goodbye 👋")help
    elif user_input.lower() == "help":
        print("""
 Supported Features:
- Basic: +, -, *, /, %, ^
- Use 'ans' to reuse previous answer
- Functions: sqrt(x), sin(x), cos(x), tan(x), log(x), abs(x)
- Example: (10 + 5) * 2, sqrt(25), 5^3, ans + 10
""")
        continue

   
    result = calculate(user_input)
    print("Result =", result)

  
    history.append(f"{user_input} = {result}")
