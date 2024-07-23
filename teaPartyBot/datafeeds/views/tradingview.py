from django.http import HttpResponse
from tvDatafeed import TvDatafeed, Interval

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def history(request, exchange, symbol):
    tv = TvDatafeed()
    # Download data
    data = tv.get_hist(symbol=symbol, exchange=exchange, interval=Interval.in_1_minute, n_bars=50400)
    return HttpResponse(data.to_json(encoding="utf-8"))
    
