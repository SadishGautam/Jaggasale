from django import forms
from .models import Item, Images


class HouseForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'title', 'location', 'area', 'category',  'rooms', 'bathrooms',
            'floors', 'Description', 'address','built_date', 'area_face', 'price', 'phone_number',
            'have_parking', 'have_garden', 'have_drinage', 'have_balcony',
            'have_hallRoom', 'have_diningRoom', 'have_elevator', 'have_water',
            'have_electricityBackup', 'have_securityStaff',
            'Ap_have_parking',
             'AP_have_electricity',
              'Ap_have_drinage',
               'Ap_have_dining_room',
                'Ap_have_kids_playground',
                 'Ap_have_lift',
                  'Ap_have_water_supply',
                   'La_have_road',
                   'La_have_electricity',
                   'La_have_drinage',
                   'La_have_water',
            'have_lift', 'have_kidsPlayground', 'have_electricityPole',
            'have_road', 'have_waterSupply','image', 'Latitude', 'Longitude', ]


        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control mt-1', 'type': 'number'}),
            'category': forms.Select(attrs={'class': 'form-control mt-1', 'type': 'number'},),
            'area': forms.NumberInput(attrs={'placeholder': 'Area', 'class': 'form-control', 'min': 0}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'rooms': forms.NumberInput(attrs={'placeholder': 'Rooms', 'class': 'form-control', 'min': 1}),
            'bathrooms': forms.NumberInput(attrs={'placeholder': 'Bathrooms', 'class': 'form-control', 'min': 1}),
            'floors': forms.NumberInput(attrs={'placeholder': 'Floors', 'class': 'form-control', 'min': 1}),
            'Description': forms.TextInput(attrs={'placeholder': 'Description', 'class': 'from-control', 'rows': 5, 'cols': '100'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form-control', 'min': 1}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'form-control'}),
            'built_date': forms.NumberInput(attrs={ 'placeholder': 'Built Date', 'class': 'form-control', 'type': "date"}),
            'area_face': forms.Select(attrs={'class': 'form-control mt-1', 'type': 'number'}),
            'Latitude': forms.TextInput(attrs={ 'class': 'form-control'}),
            'Longitude': forms.TextInput(attrs={ 'class': 'form-control'}),




        }

        # class ApartmentForm(forms.ModelForm):
        #     class Meta:
        #         model = Item
        #         fields = [
        #             'title', 'location', 'area', 'category',  'rooms', 'bathrooms',
        #             'area_face', 'Description',  'price', 'phone_number',
        #             'have_parking',  'have_drinage', 'built_date',
        #             'have_diningRoom', 'have_water',
        #             'have_electricityBackup', 'have_securityStaff',
        #             'have_lift', 'have_kidsPlayground',
        #             'image', ]
        #


        #
        # widgets = {
        #     'built_date': forms.NumberInput(attrs={ 'placeholder': 'Built Date', 'class': 'form-control', 'type': "date"}),
        #     'area_face': forms.Select(attrs={'class': 'form-control mt-1', 'type': 'number'}),
        #
        # }


class ContactForm(forms.Form):
    full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'fullname_id', 'placeholder': "First Name, Last Name",  'style': "border:none;background:none; box-shadow: none;outline:none;"}))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'email_id', 'placeholder': "Your Email",  'style': "border:none;background:none; box-shadow: none;outline:none;"}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
                            'class': 'form-control', 'id': 'phone_id', 'placeholder': "Phone",  'style': "border:none;background:none; box-shadow: none;outline:none;"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'message_id', 'placeholder': "Feel free to message us",
                                                                          'rows': '3',  'style': "border:none;background: #f8f9fa !important; box-shadow: none;outline:none;  font-family:'abel';"}))

# class AdditionalImages(forms.ModelForm):
#     image = forms.ImageField(label='Image')
#     class Meta:
#         model = Images
#         fields = [{
#
#         }'images',]

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
