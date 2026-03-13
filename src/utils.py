def generate_library_template(language, name):
    """
    Generate a library template for the specified language.
    :param language: Programming language for the library.
    :param name: Name of the library.
    """
    if language == 'python':
        return f'Creating Python library {name}...'
    elif language == 'javascript':
        return f'Creating JavaScript library {name}...'
    else:
        return 'Language not supported.'


# Example usage:
if __name__ == '__main__':
    print(generate_library_template('python', 'my_lib'))
