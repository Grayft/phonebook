import traceback


def get_executable_func_name():
    """Возвращает имя исполняемой в данный момент функции"""
    stack = traceback.extract_stack()
    return stack[-2][2]