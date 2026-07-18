def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class
    or if obj is an instance of a subclass of a_class
    """
    return isinstance(obj, a_class)
