import inspect

def display_function_name(function_) -> None:
    """
    Displays the name and file location of a given function.

    Args:
        function_ (frame): A frame object representing the function to display information for.

    Returns:
        None
    """
    
    # Retrieve the function's name and the file in which it is defined
    function_name = function_.f_code.co_name
    file_name_function = inspect.getfile(function_)
    
    # Display the function name and location in the console for tracking
    print(f'\nRunning {function_name} in {file_name_function}...')