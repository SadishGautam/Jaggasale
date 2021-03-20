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
        fields = ['title','location', 'area', 'rooms', 'bathrooms', 'floors', 'Description',  'price', 'phone_number', 'image',  ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'location': forms.Select(attrs={ 'class': 'form-control mt-1', 'type': 'number'}),
            'area': forms.TextInput(attrs={'placeholder': 'Area', 'class': 'form-control'}),
            'rooms': forms.TextInput(attrs={'placeholder': 'Rooms', 'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs={'placeholder': 'Bathrooms', 'class': 'form-control'}),
            'floors': forms.TextInput(attrs={'placeholder': 'Floors', 'class': 'form-control'}),
            'Description': forms.TextInput(attrs={'placeholder': 'Description', 'class': 'from-control', 'rows': '5'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'form-control'}),

        }



        # exclude = ('label', 'email', 'slug', 'category','sold_or_rent', 'picture_count', 'owner_name', 'phone_number', 'date', 'location', 'map', 'image')
        # title = forms.CharField(max_length=50)
        # location = forms.CharField(
        #     choices=LOCATION_LIST, max_length=2, default='Kathmandu')
        # area = forms.IntegerField()
        # rooms = forms.IntegerField()
        # bathroomrooms = forms.IntegerField( )
        # floors = forms.IntegerField()
        # description = forms.CharField(max_length=700)
        # discount_price = forms.IntegerField()
        # final_price = forms.IntegerField()
        # image = forms.ImageField(default='default.jpg', upload_to='static/images')
