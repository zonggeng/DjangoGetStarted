from django.shortcuts import render
from .models import UserMessage


# Create your views here.

def getform(request):
    # UserMessage默认的数据管理器objects。
    # 方法all()是将所有数据返回成一个queryset类型(django的内置类型)
    all_message = UserMessage.objects.all()
    # 按条件获取
    # all_message = UserMessage.objects.filter(name=' 黄宗更', address='广东省广州市番禺区')

    # 删除操作 根据条件获取到后调用delete删除
    # all_message.delete()
    # 我们可以对于all_message进行遍历操作
    for message in all_message:
        # 每个message实际就是一个UserMessage对象（这时我们就可以使用对象的相关方法）。
        print(message.name)
        # 可以用if判断然后 message.delete()

    """
    # 存储部分
    user_message = UserMessage()

    # 为对对象真假属性
    user_message.name = '卢晓芳'
    user_message.message = '你怎么那么丑'
    user_message.address = '广东省揭阳市玉白村'
    user_message.email = '13537419055@qq.com'
    user_message.object_id = 'efgh'

    # 调用sace方法进行保存
    user_message.save()
    """

    """
    # 从页面获取数据并保存到数据库
    if request.method == "POST":
        # 就是取字典里key对应value值而已。取name，取不到默认空
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        # 创建对象
        user_message = UserMessage()
        # 将html的值传入我们实例化的对象.
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "ijkl"

        # 调用save方法进行保存
        user_message.save()
        """

    return render(request, 'message_form.html')
