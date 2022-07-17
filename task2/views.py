import operator
from rest_framework.decorators import api_view
from datetime import date
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

dt = date.today()


@api_view(http_method_names=['GET'])
def today(request):
    return Response({'date': dt.strftime('%d/%m/%Y'), 'year': dt.year, 'month': dt.month, 'day': dt.day})


@api_view(http_method_names=['GET'])
def hello_world(request):
    return Response({'msg': 'Hello World'})


# http://127.0.0.1:8000/task2/my_name/?name=Maks
@api_view(http_method_names=['GET'])
def my_name(request):
    try:
        name_of_hacker = request.query_params['name']
        print('request', request)
        print("request.query_params", dict(request.query_params))
        return Response({'name': name_of_hacker})
    except KeyError:
        raise ValidationError


# Test data
# {
#     "action": "minus",
#     "number1": 15,
#     "number2": 10
# }
@api_view(http_method_names=['POST'])
def calculator(request):
    actions = {'minus': operator.sub, 'plus': operator.add, 'divide': operator.truediv, 'multiply': operator.mul}
    data = request.data
    action = data['action']
    number1 = int(data['number1'])
    number2 = int(data['number2'])
    if action not in actions:
        raise ValidationError(f'{action} not in action list')
    else:
        try:
            result = actions[action](number1, number2)
        except ZeroDivisionError:
            raise ValidationError('Zero division!')
    return Response({'result': result})
