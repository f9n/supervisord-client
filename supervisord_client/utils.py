import functools
import xmlrpc.client


def handle_exceptions(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except xmlrpc.client.Fault as err:
            return False, err.faultString
        except Exception as err:
            return False, str(err)

    return wrapped
