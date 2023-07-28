from django import forms 
from .models import ipfs,team,capture,buy_energy,meter_analytics,summary_file,meta_video,forum,cloud

class teamForm(forms.ModelForm):
    class Meta:
        model=team
        fields=[
            'member',
            'memid',
            'location',
            'memberGen',
            'age',
            'adhaar',
        ]

class forumForm(forms.ModelForm):
    class Meta:
        model=forum
        fields=[
            'user_name',
            'answer',
        ]

class vidForm(forms.ModelForm):
    class Meta:
        model=capture
        fields=[
            'date',
        ]


class cloudForm(forms.ModelForm):
    class Meta:
        model=cloud
        fields=[
            'p_num',
            'p_name',
        ]

# class hashForm(forms.ModelForm):
#     class Meta:
#         model = UploadFile
#         fields = [
#             'uploadfile_name',
#         'uploadfile', 
        
#         ]

class buyForm(forms.ModelForm):
    class Meta:
        model = buy_energy
        fields = [
            'cus_name',
            'meter_id',
            'quantity',
            'energy_price',
        ]


class meterForm(forms.ModelForm):
    class Meta:
        model = meter_analytics
        fields = [
            'res',
           
        ]
class ipfsForm(forms.ModelForm):
    class Meta:
        model = ipfs
        fields = [
            'f_hash',
           
        ]

class summForm(forms.ModelForm):
    class Meta:
        model = summary_file
        fields = [
            'p_name',
            'p_num',
           
        ]
    
class vidForm(forms.ModelForm):
    class Meta:
        model = meta_video
        fields = [
            'pv_name',
            'pv_num',
           
        ]