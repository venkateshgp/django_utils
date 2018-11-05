from django.http import JsonResponse


def eim_response(status_code=201, ve=[],ie=[], success = 'yes', s_msgs=[], err_msgs=[], ret={}):
    """ve > Provide valid entries from UI form or from request body
        ie > Provide invalide entries from request body
        msgs > Custom Messages in key value format(Its a dictionary).
        ret > This will be API endpoint data
        success > 'yes' or 'no' values
        s_msgs > Success messages, you can also make list of message dictionaries
        err_msgs > Error messages, you can also make list of message dictionaries
        ret > API response data
        status_code > request status code, its a must parameter.
    """
    resp ={}
    if ve!=[]:
        resp['Valid_entries'] = ve
    if ie != []:
        resp['Invalid_entries'] = ie
    if err_msgs != []:
        resp['error_msgs'] = err_msgs
    resp['Data'] = ret
    resp['status_code'] = status_code
    if status_code in range(200,299):
        s_msgs = [{
            "Message": "Request is processed",
        }]
    if s_msgs != []:
        resp["Success_Messages"] = s_msgs
    resp ["Success"] = success
    resp = JsonResponse(resp, status=status_code)
    return resp
