from typing import Callable, Any, Optional

def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            msg = f"{func.__name__} started"
            if filename:
                with open(filename, 'a') as f:
                    f.write(msg + '\n')
            else:
                print(msg)
            result = func(*args, **kwargs)
            msg = f"{func.__name__} finished"
            if filename:
                with open(filename, 'a') as f:
                    f.write(msg + '\n')
            else:
                print(msg)
            return result
        return wrapper
    return decorator

@log()
def hello_world() -> str:
    return "hello world!"

hello_world()