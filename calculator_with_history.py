HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("NO history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared.')
        
def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a') 
    
    file.write(equation + "=" + str(result) + "\n")
    file.close()
    
def calculate(user_input):
    import re
    if not re.match(r'^[\d+\-*/. ()^]+$', user_input):
        print('Invalid input. Use format: number operator number (e.g. 8 + 8)')
        return
    user_input = user_input.replace('^', '**')
    try:
        result = eval(user_input)
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return
    except Exception:
        print("Invalid input. Please check your expression.")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

    
def main():
    print('---SIMPLE CALCULATOR (type history, clear or exit)') 
    while True:        
        user_input = input("ENTER calculation(+ - * /) or command (history,clear,exit)=")
        if user_input == 'exit':
            print('Goodbye')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
            
main()