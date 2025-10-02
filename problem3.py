def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    numbers = []
    while True:
        input_value = input("Enter a number (or 'done' to finish): ")
        if input_value == 'done':
            break
        try:
            n = float(input_value)
            numbers.append(n)
        except ValueError:
            print("Invalid input value. Please enter a valid number or the word 'done'.")
    return numbers




def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers
    """
    if not numbers:
        return None

    analysis = {}
    analysis['count'] = len(numbers)
    analysis['sum'] = sum(numbers)
    analysis['average'] = analysis['sum'] / analysis['count']
    analysis['minimum'] = min(numbers)
    analysis['maximum'] = max(numbers)

    # Count even and odd numbers iff integers
    even_count = 0
    odd_count = 0
    for c in numbers: #check if number is a whole integer
        if isinstance(c, int) or c.is_integer():
            # Conversion of float integers to int
            if int(c) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        analysis['even_count'] = even_count
        analysis['odd_count'] = odd_count    
        
    return analysis




def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    if analysis is None:
        print("No data analyzed.")
    else:
        print("Analysis")
        print(f"Count       : {analysis['count']}")
        print(f"Sum         : {analysis['sum']:.2f}")
        print(f"Average     : {analysis['average']:.2f}")
        print(f"Minimum     : {analysis['minimum']}")
        print(f"Maximum     : {analysis['maximum']}")
        print(f"Even Count  : {analysis['even_count']}")
        print(f"Odd Count   : {analysis['odd_count']}")
    pass




def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")

    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)

if __name__ == "__main__":
    main()