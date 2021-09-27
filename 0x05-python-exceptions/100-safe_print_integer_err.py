#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        import sys
        print("{:d}".format(value))
        return True
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        return False
