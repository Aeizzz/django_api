from django.views.decorators.csrf import csrf_exempt
from utils.api.api import APIView, validate_serializer
from .models import TimeLine
from .serializers import CreateTimeLineSerializer,TimeLineSerializer

# Create your views here.

'''
完成时间轴的增删改查
'''
class TimeLineAPI(APIView):
    @validate_serializer(CreateTimeLineSerializer)
    def post(self,request):
        data = request.data
        timeline = TimeLine.objects.create(**data)
        return self.success(TimeLineSerializer(timeline,many=True).data)

    def get(self,request):
        '''
        获取全部和获取一个
        :param request:
        :return:
        id
        '''
        timeline = TimeLine.objects.all()
        id = request.GET.get('id')
        if id:
            timeline = timeline.get(id=id)

        return self.success(TimeLineSerializer(timeline,many=True).data)


    def put(self,request):
        pass

    def delete(self,request):
        id = request.GET.get('id')
        try:
            timeline = TimeLine.objects.get(id=id)
        except TimeLine.DoesNotExist:
            return self.error('timelinr Does Not Exist')
        timeline.delete()
        return self.success()