from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <section>
        Hello, One prototyped WebUI for Tea-Party Bot.</br>

        <button>Marktdaten sammeln</button> Bestimme das Symbol und den Exchange um die Marktdatenabzurufen.</br>

        <button>Bot erstellen</button> Erstelle deinen Bot mit unterschiedlichen Strategien.</br>
        <button>Backtesting</button> Backteste den Teapartybot mit verschiedenen Parametern. Der Bot waehlt dem
                    vorgegebenen Rahmen selbstaendig Paramter fuer den Bot und vergleicht Anschliessend die Ergebnisse.</br>

        <button>Bot Trading</button> Sobald du eienen rentablen Bot erstellt hast, kannst du ihn zum live Traden aktiveren.</br>
        </section>
        """)

def bot_create(request):
    return HttpResponse("""
    <section>
    Erstelle deinen Bot.</br>
    <label>Name des Bots:</label><input></input></br> 
    <label>Marktdaten Quelle:</label><input></input></br>
    <label>Strategien:</label> <div class='dropdown'><option><item></item></option></div>
    </section>
                        """)

def backtest(request):
    return HttpResponse("Backteste deinen Bot.")
