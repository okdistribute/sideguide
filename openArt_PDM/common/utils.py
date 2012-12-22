from django.http import HttpResponse
from django.utils import simplejson as json
from django.utils.encoding import smart_str
from django.utils.hashcompat import sha_constructor

def response400(problem, details):
    response = {
        'problem' : problem,
        'details' : details
        }
    response_status = 400
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def response401():
    response = {
        'problem' : 'Not Authorized',
        'details' : ''
        }
    response_status = 401
    return HttpResponse(json.dumps(response), mimetype="application/json", status=response_status)

def get_hexdigest(algorithm, salt, raw_password):
    """
    Returns a string of the hexdigest of the given plaintext password and salt
    using the given algorithm ('md5', 'sha1' or 'crypt').
    """
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return md5_constructor(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha_constructor(salt + raw_password).hexdigest()
    raise ValueError("Got unknown password algorithm type in password.")

def authenticated(request):
    #need to implement
    return True
