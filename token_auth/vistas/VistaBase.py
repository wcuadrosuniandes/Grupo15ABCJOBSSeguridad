from functools import wraps
from flask_jwt_extended import (
    get_jwt,
    verify_jwt_in_request,
)

from modelos import (
    UserToken
)

user_token = UserToken()


def candidate_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_candidate"]:
                return fn(*args, **kwargs)
            else:
                return {"mensaje": "No autorizado"}, 403

        return decorator

    return wrapper


