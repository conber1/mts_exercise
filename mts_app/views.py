from django.shortcuts import redirect
import roundrobin
from urllib.parse import urlparse

SERVERS = ["ORIGIN", "CDN_A", "CDN_B"] #list of the nodes

get_roundrobin = roundrobin.basic(SERVERS) 

def redirect_to_server(request): #function which redirect us to new server depending on previous server
    new_state = get_roundrobin()
    message = request.GET.get('video') #getting the parametr of the link *video* 
    data = urlparse(message) #getting needed part of the URL
    if new_state == "ORIGIN": #if server doesn't changes then redirect to this server
        return redirect(message)
    else: #if user is going in cdn then redirect to url below
        return redirect(f"https://{new_state}{data.path}{data.query}") 

