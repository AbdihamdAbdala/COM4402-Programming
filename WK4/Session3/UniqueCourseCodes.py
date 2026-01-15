def enrol_module(modules, code):
    """Add a module code if not already present."""
    modules.add(code)


def is_enrolled(modules, code):
    """Return True if the student is enrolled on this module."""
    return code in modules


def drop_module(modules, code):
    """Remove a module if present."""
    modules.discard(code)


def count_modules(modules):
    """Return how many modules the student is taking."""
    return len(modules)


modules = set()

enrol_module(modules, "COM4402")
enrol_module(modules, "COM4403")
enrol_module(modules, "COM4404")

print(is_enrolled(modules, "COM4402"))
print(count_modules(modules))

drop_module(modules, "COM4403")
print(count_modules(modules))