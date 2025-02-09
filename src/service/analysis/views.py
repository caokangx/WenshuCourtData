import pandas
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from io import StringIO
from doc_classification import classify_doc
from request import upload_doc_to_backend
from .apps import cnn_model, max_file_size
from product_ner import do_prod_ner


# Create your views here.
@csrf_exempt
def upload(request):
    data = {}
    if "GET" == request.method:
        return 'None'

    csv_file = request.FILES["uploadedFile"]
    if not csv_file.name.endswith('.csv'):
        msg = 'File is not CSV type'
        return JsonResponse({
            'msg': msg
        }, status=400)

    # if file is too large, return
    if csv_file.multiple_chunks(chunk_size=max_file_size):
        msg = "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000))
        return JsonResponse({
            'msg': msg
        }, status=400)

    file_data = csv_file.read().decode("utf-8")

    data_str_io = StringIO(file_data)
    df = pandas.read_csv(data_str_io, keep_default_na=False)
    df = classify_doc(cnn_model, df)
    data_list = do_prod_ner(df)

    responseJson = upload_doc_to_backend(data_list)
    return JsonResponse(responseJson)
