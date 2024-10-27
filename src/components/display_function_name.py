import inspect

def display_function_name(function_) -> None:
    # Mendapatkan nama fungsi secara dinamis
    function_name = function_.f_code.co_name
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(function_)
    print(f'\nRunning {function_name} in {file_name_function}...')