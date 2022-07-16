import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from .models import People, City, Job


def home(request):
    return HttpResponse("<h2>Hello, world. <br> Все работает, я рад!!!</h2>")


def import_csv(request):
    """Загрузка файла в базу данных"""
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            empexceldata = pd.read_csv("." + excel_file, encoding='utf-8')
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                city = City.objects.update_or_create(name=dbframe.city)
                job = Job.objects.update_or_create(name=dbframe.job)
                product = People.objects.get_or_create(name=dbframe.name, age=dbframe.age, email=dbframe.email,
                                                       city_id=city.id, job_id=job.id)
                print(product, 'Что отправилось')
            return render(request, 'importexcel.html', {'uploaded_file_url': uploaded_file_url})
    except Exception as identifier:
        print(identifier)
    return render(request, 'importexcel.html', {})


def export_csv(request):
    """Получение файла из базы данных"""
    if request.method == 'POST':
        response = HttpResponse(content_type='')
        response['Content-Disposition'] = 'attachment; filename="DB.xlsx"'  # Название полученного файла из базы данных
        writer = csv.writer(response)
        writer.writerow(['name', 'age', 'email', 'city', 'job'])  # Название колонок в Excel файле
        users = People.objects.all().values_list('name', 'age', 'email', 'city__name', 'job__name')
        for user in users:
            writer.writerow(user)
        return response
    return render(request, 'exportexcel.html')
