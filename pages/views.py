from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {
            'menu': [
                {'url': '#about', 'text': 'Обо мне'},
                {'url': '#', 'text': 'Портфолио'},
                {'url': '#', 'text': 'Контакты'},
            ],
            'about': {
                'photo': 'photo.jpg',
                'fullname': 'Бурков Денис',
                'text': 'Моим родным городом является Магнитогорск. Учусь в СУНЦ УрФУ уже третий год в инф-мат классе. Увлекаюсь програмированием, математикой и книгами. При решении каких-либо задач имею тягу создать максимально универсальное решение. В свободное от учебы время занимаюсь попытками написать что-либо практически применимое.'
            }
    }
