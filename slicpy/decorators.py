import os
import functools
from datetime import datetime
import inspect
class Logger:
    def __init__(self, log_path):
        self.log_path = '@logs/'+ log_path
        
        try:
            os.mkdir('@logs')
        except:
            pass
        self.create_log_file()

    def create_log_file(self):
        if not os.path.exists(self.log_path):

            open(self.log_path, 'w').write("")
       

    def log(self, message):
        with open(self.log_path, 'a') as f:
            f.write(f"{message}")

    def decorator(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                function_params = inspect.signature(func).parameters
                param_names = [param.name for param in function_params.values()]
 
                param_values = list(args) + list(kwargs.values())
                params = dict(zip(param_names, param_values))
                print(params)
                message = f"INFO: {func.__name__} ||  params {[params]} || @ object - {func} executed successfully"
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                message=  f"[{timestamp}] - {message}\n"
                print(message)
                self.log(message)
                return result
            except Exception as e:
                self.log(f"ERROR: {func.__name__} failed: {str(e)}")
                raise
        return wrapper

 

class CLeanLogger:
    def __init__(self, log_path):
        self.log_path = '@logs/' + log_path
        self.create_log_file()
        try:
            os.mkdir('@logs')
        except:
            pass

    def create_log_file(self):
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                f.write("")

    def log(self, message):
        with open(self.log_path, 'a') as f:
            f.write(f"{message}\n")

    def log_info(self, func, params):
        message = f"INFO: {func.__name__} ||  params {[params]} || @ object - {func} executed successfully"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message=  f"[{timestamp}] - {message}"
        self.log(message)

    def log_error(self, func, error):
        message = f"ERROR: {func.__name__} failed: {str(error)}"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message=  f"[{timestamp}] - {message}"
        self.log(message)

    def log_function(self, func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            function_params = inspect.signature(func).parameters
            param_names = [param.name for param in function_params.values()]
            param_values = list(args) + list(kwargs.values())
            params = dict(zip(param_names, param_values))
            self.log_info(func, params)
            return result
        except Exception as e:
            self.log_error(func, e)
            raise
