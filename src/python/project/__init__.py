import atexit


def shutdown():
    print("project module shutdown")


atexit.register(shutdown)

print("project module loaded.")
