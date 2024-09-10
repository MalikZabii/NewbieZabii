
import traceback


def debug_function(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print("An error occurred:")
            print("Exception type:", type(e).__name__)
            print("Exception message:", str(e))
            print("Traceback:")
            traceback.print_exc()
            # Optionally log to a file
            with open("debug_log.txt", "a") as f:
                f.write("Exception type: {}\n".format(type(e).__name__))
                f.write("Exception message: {}\n".format(str(e)))
                f.write("Traceback:\n")
                traceback.print_exc(file=f)
            return None
    return wrapper


@debug_function
def example_function(x):
    return 10 / x


# Test with a value that will cause an error
example_function(0)
