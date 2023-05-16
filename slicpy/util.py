import os
import functools
from datetime import datetime
class Util(object):
    @staticmethod
    def fullmatch(pattern,string):
        metacharacters = {'.', '*', '+', '?', '{', '}', '[', ']', '(', ')', '|', '^'}

        def match_here(pattern, string):
            if not pattern:
                return True
            elif pattern[0] == '$':
                return len(string) == 0 and match_here(pattern[1:], string)
            elif len(pattern) > 1 and pattern[1] == '*':
                return match_star(pattern[0], pattern[2:], string)
            elif len(pattern) > 1 and pattern[1] == '+':
                return match_plus(pattern[0], pattern[2:], string)
            elif len(pattern) > 1 and pattern[1] == '?':
                return match_question(pattern[0], pattern[2:], string)
            elif pattern[0] == '\\':
                return string and string[0] == pattern[1] and match_here(pattern[2:], string[1:])
            elif not string:
                return False
            elif pattern[0] not in metacharacters:
                return string[0] == pattern[0] and match_here(pattern[1:], string[1:])
            else:
                return False

        def match_star(c, pattern, string):
            if match_here(pattern, string):
                return True
            if c == '.':
                return any(match_star(c, pattern, string[i:]) for i in range(1, len(string) + 1))
            return any(string[i] == c and match_star(c, pattern, string[i:]) for i in range(len(string)))

        def match_plus(c, pattern, string):
            if c == '.':
                return any(match_here(pattern, string[i:]) for i in range(1, len(string) + 1))
            return any(string[i] == c and match_here(pattern, string[i:]) for i in range(len(string)))

        def match_question(c, pattern, string):
            if c == '.':
                return match_here(pattern, string) or match_here(pattern, string[1:])
            return (string and string[0] == c and match_here(pattern, string[1:])) or match_here(pattern, string)

        return match_here(pattern, string)
    @staticmethod
    def handle_buffer(input):
        # 10

        try:
        
            result = eval(input, {"__builtins__": None}, {"True": True, "False": False, "None": None})
        except Exception as e:
            raise ValueError(f"Failed to evaluate the input string: {e}")

        return result
    
    @staticmethod
    def mkdir(dir):
        try:
            os.mkdir(dir)
        except:
            pass
    @staticmethod
    def timestamp():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def ipkey(addr):
        return f"{addr[0]}:{str(addr[1])}"
    @staticmethod
    def get_nested_attribute(r,obj, attr_list):
        bits = f"{r[0]} - {obj}\n"
        for attr in range(len(attr_list)):
            obj1 = getattr(obj, attr_list[attr])
            bits += f"{r[attr]} - {obj1}\n"
        return bits