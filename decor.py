def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if e is None:
                return "Enter the argument for the command. Give me name and phone or birthday, please."
            else:
                return f"Error: {e}"
        except KeyError as e:
            if e is None:
                return "No such name found"
            else:
                return f"Error: {e}"
        except IndexError as e :
            if e is None:
                return "Enter the argument for the command. Give me name, please."
            else:
                return f"Error: {e}"
        except Exception as e:
            return f"Error: {e}"

    return inner
