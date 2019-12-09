from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'treasures' : treasures})

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",'https://placekitten.com/150/100'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO",'https://placekitten.com/150/100'),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA','https://placekitten.com/150/100'),
]
