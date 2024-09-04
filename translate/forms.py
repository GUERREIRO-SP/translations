from django import forms

class RegisterForms(forms.Form):
    strategy_list = ['ChatGPT', 'Google', 'Manual']
    language_list = ['en-us', 'es-419', 'pt-br']

    id = forms.CharField(
        label = "id",
        required = True,
        max_length = 36,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "uuID7"
            }
        )
    )
    id_project = forms.CharField(
        label = "id_project",
        required = True,
        max_length = 36,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "uuID7"
            }
        )
    )
    key = forms.CharField(
        label = "key",
        required = True,
        max_length = 255,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    # strategy = forms.ChoiceField(choices=strategy_list, required=True)
    # language = forms.ChoiceField(choices=language_list, required=True)
    strategy = forms.CharField(
        label = "strategy",
        required = True,
        max_length = 255,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    language = forms.CharField(
        label = "language",
        required = True,
        max_length = 25,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    context = forms.CharField(
        label = "context",
        required = True,
        max_length = 1000,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    value = forms.CharField(
        label = "value",
        required = True,
        max_length = 1000,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    override_en = forms.CharField(
        label = "override_en",
        required = True,
        max_length = 1000,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    flag_export = forms.BooleanField()

    # senha = forms.CharField(
    #     label = "Senha",
    #     required = True,
    #     max_length = 70,
    #     widget = forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Digite sua senha"
    #         }
    #     )
    # )
