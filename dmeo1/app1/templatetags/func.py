from django import template
from ..models import AddImg,GmaeInfo,CategroyInfo,Comment
register=template.Library()

@register.filter()
def Delstr(value,num):
    return value[:num]



@register.simple_tag()
def GetAds():
    return AddImg.objects.all()

@register.simple_tag()
def GetHotGames(num = 6 ):
    if num == 6:
        num=GmaeInfo.objects.all().count()
        return GmaeInfo.objects.all()[:num]
    else:
        return GmaeInfo.objects.all().order_by('-ReadNum')[:num]


@register.simple_tag()
def GetNewGames(num=8):
    return GmaeInfo.objects.all().order_by('-Creat_Time')[:num]

@register.simple_tag()
def GetCategroyInfo():
    return CategroyInfo.objects.all()

@register.simple_tag()
def Getcomments(id):
    print(id)
    return Comment.objects.filter(pk=id)



