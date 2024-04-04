def print_message(start_message, end_message):
    def inner_decorator(method_to_decorate):
        def wrapper(self):
            print(start_message)
            method_to_decorate(self)
            print(end_message)

        return wrapper

    return inner_decorator
