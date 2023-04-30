from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_dept(request):
    if request.method=='POST':
        DEPTNO=request.POST['deptno']
        DNAME=request.POST['name']
        LOC=request.POST['loc']
        DO=Dept.objects.get_or_create(DEPTNO=DEPTNO,DNAME=DNAME,LOC=LOC)[0]
        DO.save()
        return HttpResponse('Dept is inserted Successfully')

    return render(request,'insert_dept.html')


def insert_emp(request):
    LOD=Dept.objects.all()
    d={'deptdata':LOD}
    if request.method=='POST':
        EMPNO=request.POST['empno']
        ENAME=request.POST['ename']
        JOB=request.POST['job']
        MGR=request.POST['mgr']
        HIREDATE=request.POST['hiredate']
        SAL=request.POST['sal']
        COMM=request.POST['comm']
        DEPTNO=request.POST['deptno']
        DO=Dept.objects.get(DEPTNO=DEPTNO)
        EO=Emp.objects.get_or_create(EMPNO=EMPNO,ENAME=ENAME,JOB=JOB,MGR=MGR,HIREDATE=HIREDATE,SAL=SAL,COMM=COMM,DEPTNO=DO)[0]
        EO.save()
        return HttpResponse('emp is inserted Successfully')
    return render(request,'insert_emp.html',d)