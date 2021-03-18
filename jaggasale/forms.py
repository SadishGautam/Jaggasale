from django import forms
from .models import Item

LOCATION_LIST = (
    ('K', 'Kathmandu'),
    ('L', 'Lalitpur'),
    ('L', 'Bhaktapur'),
    ('C', 'Chitwan'),

)

class HouseForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('label', 'email', 'slug', 'category','sold_or_rent', 'picture_count', 'owner_name', 'phone_number', 'date', 'location', 'map', 'image')
        title = forms.CharField(max_length=50)
        # location = forms.CharField(
        #     choices=LOCATION_LIST, max_length=2, default='Kathmandu')
        area = forms.IntegerField()
        rooms = forms.IntegerField()
        bathroomrooms = forms.IntegerField( )
        floors = forms.IntegerField()
        description = forms.CharField(max_length=700)
        discount_price = forms.IntegerField()
        final_price = forms.IntegerField()
        # image = forms.ImageField(default='default.jpg', upload_to='static/images')
