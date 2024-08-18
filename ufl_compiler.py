def evaluate_expression(expr, variables):
    try:
        # Define a safe evaluation environment with the variables
        safe_env = {**variables}
        result = eval(expr, {"__builtins__": None}, safe_env)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_line(line, variables):
    line = line.strip()

    if line.startswith('//') or not line:
        # Skip comments and empty lines
        return
    
    if line.startswith('let '):
        # Variable assignment
        _, var, value = line.split(' ', 2)
        var, value = var.strip(), value.strip()
        try:
            value = eval(value, {"__builtins__": None})
        except Exception as e:
            print(f"Error evaluating value for {var}: {e}")
            return
        variables[var] = value
        return
    
    if line.startswith('ifthis '):
        # Conditional statement
        condition = line[7:].strip()
        if evaluate_expression(condition, variables):
            print("Condition met.")
        else:
            print("Condition not met.")
        return
    
    if line.startswith('orelse'):
        # Handle 'orelse' logic (alternative branch in conditions)
        print("Else condition.")
        return
    
    if line.startswith('foreverloop '):
        # Infinite loop (basic implementation)
        parts = line.split(' ', 1)
        loop_body = parts[1]
        while True:
            process_line(loop_body, variables)
        return

    if line.startswith('say '):
        # Print statement
        message = line[4:].strip().strip('"')
        print(message)
        return

    # Handle unknown commands
    print(f"Unknown command: {line}")

def interpret_ufl(file_path):
    variables = {}
    try:
        with open(file_path, 'r') as file:
            accumulated_line = ""
            for line in file:
                line = line.strip()
                
                if line.endswith('\\'):
                    # Accumulate lines ending with line continuation
                    accumulated_line += line[:-1]  # Remove the '\\' and continue
                else:
                    accumulated_line += line
                    process_line(accumulated_line, variables)
                    accumulated_line = ""
    except Exception as e:
        print(f"Error interpreting file '{file_path}': {e}")

# Example usage
if __name__ == "__main__":
    interpret_ufl('C:/Users/isaac/Miscellanious/UFL/example.ufl')
