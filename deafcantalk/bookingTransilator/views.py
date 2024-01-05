from django.shortcuts import render
from .models import Languages, Booking, VideoContent
from .forms import BookingForm
# Create your views here.
def index(request):
    video_content = VideoContent.objects.all() 
    form = BookingForm()


    context = {
        'video_content':video_content,
        'form':form
    }
    
    return render(request, 'booking/index.html', context)

def book_translator(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'booking/thankyou.html', {'thank_you': True})
    else:
        form = BookingForm()
            
    return render(request, 'booking/index.html')
