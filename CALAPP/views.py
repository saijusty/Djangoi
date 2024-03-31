from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Demo(request):
    output=""
    if request.method=="POST":


        num3=eval(request.POST.get("fnum"))
        num4=eval(request.POST.get("snum"))
        opr=request.POST.get("opr")

        dictkey = {"+":num3+num4,"*":num3*num4,"/":num3/num4,"-":num3-num4}

        for i in dictkey.keys():
            if opr in i:
                output=dictkey[i]
    return render(request,"calform.html",{'result':output})
            
""" 
        if opr=="+":
            output=num3+num4
        if opr=="-":
            output=num3-num4
        if opr=="*":
            output=num3*num4
        if opr=="/":
            output=num3/num4 """

        

    
