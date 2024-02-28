from django.http import JsonResponse
from pharmacy.models import Cure


def ping(request):
    data = {'message': 'Server is up and running'}
    return JsonResponse(data)


cures = [
    Cure(1, 'Citramon', 50, 'For headache', 10, True).__dict__,
    Cure(id=2, title='Paracetomol', price=30, description='For cold', amount=0, is_cure=False).__dict__,
    Cure(id=3, title='Doctor Mom', price=100, description='For throat', amount=50, is_cure=True).__dict__
]


# def get_all_cures(request):
#     all_cures = []
#     for cure in cures:
#         clean_cure = {key: value
#                       for key, value in cure.items()
#                       if key != '_state'}
#         all_cures.append(clean_cure)
#     return JsonResponse(all_cures, safe=False)

def get_all_cures(request):
    for cure in cures:
        del cure['_state']
    return JsonResponse(cures, safe=False)
