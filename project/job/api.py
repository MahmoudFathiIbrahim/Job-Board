# www.django-rest-framework.org/api-guide
# views for api

# we have 3 types of views

# 1- Function Based Views :
#   - is simple
#   - easy to customize
#   - easy to apply complex logic

# 2- Class Based Views :
#   - fast development
#   - easy to customize
#   - not good for complex logic


# 3- Viewsets :
#   - api get the model and url then create all CRUD operations
#   - hard to customize



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Job
from .serializers import JobSerializer


@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data  # many=True: means there are a lot of data
    context = {'data': data}
    return Response(context)


@api_view(['GET'])
def job_detail_api(request, id):
    job_d = Job.objects.get(id=id)
    data = JobSerializer(job_d).data
    context = {'data': data}
    return Response(context)


class JobListApi(generics.ListAPIView):
    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

