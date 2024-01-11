from django.shortcuts import render , redirect , get_object_or_404
from authenticationapp.models import User , Profile
from sellerapp.models import Property
from .models import Booking
from .forms import BookingForm
from django.db.models import Q 
from datetime import datetime , timedelta


# Create your views here.

def Home(request):
    prop = Property.objects.all()
    return render(request,'home.html',{'prop':prop})



def BookingView(request, id):
    prop = get_object_or_404(Property, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            whom = Profile.objects.get(user=request.user)
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']            
            availability = Booking.objects.filter(bookfor=prop,date_from__lte=date_to,date_to__gte=date_from)
        
            if availability.exists():
                form.add_error('date_to', "This Date is Not Available. Please choose another date.")
            else:
                pays = int(prop.rate)
                strd = datetime.strptime(str(date_from),'%Y-%m-%d').date()
                endd = datetime.strptime(str(date_to),'%Y-%m-%d').date()
                duration = (endd - strd).days
                total_rate = pays * duration
                Booking.objects.create(bookfor=prop,date_from=date_from,date_to=date_to,tenant=request.user,duration=duration,total_rate=total_rate)
                userobj = Booking.objects.filter(tenant=request.user)
                return render(request,'booking_success.html',{'userobj':userobj})
    else:
        form = BookingForm()

    form.fields['bookfor'].initial = prop
    return render(request,'bookingpg.html',{'form':form,'property':prop})


def SearchView(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        properties = Property.objects.filter(
            Q(category__icontains=query) | 
            Q(rate__icontains=query) |
            Q(location__icontains=query) 
        )
        return render(request,'search_result.html',{'properties':properties})
    
    prop = Property.objects.all()
    return render(request,'home.html',{'prop':prop})


