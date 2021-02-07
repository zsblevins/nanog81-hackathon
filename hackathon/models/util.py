from hackathon.models import get_session


def session_write(func):
    """Create a decorator for wrapping a function in a session with commit."""

    def wrapper(*args, **kwargs):
        kwargs['commit'] = True
        return session_wrapper(func, *args, **kwargs)

    return wrapper


def session_read(func):
    """Create a decorator for wrapping a function in a session without commit."""

    def wrapper(*args, **kwargs):
        kwargs['commit'] = False
        return session_wrapper(func, *args, **kwargs)

    return wrapper


def session_wrapper(func, *args, **kwargs):
    """Session handling wrapper."""
    commit = kwargs.pop('commit')
    session = kwargs.get('session')

    # This call was contained in another transaction, skip transaction handling
    if session:
        return func(*args, **kwargs)

    session = get_session()

    kwargs['session'] = session

    try:
        return_value = func(*args, **kwargs)
        if commit:
            session.commit()

        return return_value
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()
