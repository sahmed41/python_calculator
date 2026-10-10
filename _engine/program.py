is_running = True

def user_input(prompt, exit_code):
    num = input(prompt)
    if num.lower() == exit_code: 
        is_running = False
        return is_running
    else:
        return float(num)
                
