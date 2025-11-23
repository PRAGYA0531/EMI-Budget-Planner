def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
