from django.shortcuts import render
from .forms import MedicineDetailsFrom
from .models import Medicine

# Create your views here.
def searchMed(request):
    if request.method == "POST":
        final_list = []
        text_val = request.POST['text']
        medicine_val = Medicine.objects.all().values_list('Medname', flat=True)
        print(medicine_val)
        final_list = [item for item in text_val.split() if item.title() in medicine_val]
        print(final_list)
        fm = MedicineDetailsFrom()
    else:
        fm = MedicineDetailsFrom()
    return render(request, 'extractmed/base.html', {'form' : fm})