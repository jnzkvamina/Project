def active_operation(operation):
    global active_operations
    active_operations=[]
    def wrapper(*args, **kwargs):
        if operation.__name__ not in active_operations:
            active_operations.append(operation.__name__)
        return operation(*args, **kwargs)    
    wrapper.active_operations = active_operations
    return wrapper
    
