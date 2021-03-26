from django import forms
from .models import Item, Images

LOCATION_LIST = (
    ('K', 'Kathmandu'),
    ('L', 'Lalitpur'),
    ('L', 'Bhaktapur'),
    ('C', 'Chitwan'),

)


class HouseForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
        # 'user',
        'title', 'location', 'area', 'rooms', 'bathrooms',
                  'floors', 'Description',  'price', 'phone_number',
                  'have_parking', 'have_garden', 'have_drinage', 'have_balcony',
                  'have_hallRoom','have_diningRoom', 'have_elevator', 'have_water',
                  'have_electricityBackup', 'have_securityStaff',
                  'have_lift', 'have_kidsPlayground', 'have_electricityPole',
                  'have_road', 'have_waterSupply', 'image', ]


        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control mt-1', 'type': 'number'}),
            'area': forms.NumberInput(attrs={'placeholder': 'Area', 'class': 'form-control', 'min': 0}),
            'rooms': forms.NumberInput(attrs={'placeholder': 'Rooms', 'class': 'form-control', 'min': 1}),
            'bathrooms': forms.NumberInput(attrs={'placeholder': 'Bathrooms', 'class': 'form-control', 'min': 1}),
            'floors': forms.NumberInput(attrs={'placeholder': 'Floors', 'class': 'form-control', 'min': 1}),
            'Description': forms.TextInput(attrs={'placeholder': 'Description', 'class': 'from-control', 'rows': 5, 'cols': '100'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form-control', 'min': 1}),
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
