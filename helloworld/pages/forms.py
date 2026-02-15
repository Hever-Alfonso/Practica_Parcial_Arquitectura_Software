from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")

        return price