from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {
            'menu': [
                {'url': '#about', 'text': 'Обо мне'},
                {'url': '#portfolio', 'text': 'Портфолио'},
            ],
            'about': {
                'photo': 'photo.jpg',
                'fullname': 'Бурков Денис',
                'text': 'Моим родным городом является Магнитогорск. Учусь в СУНЦ УрФУ уже третий год в инф-мат классе. Увлекаюсь програмированием, математикой, книгами и линукс. Люблю добавлять не запланированный функционал к устройствам. При решении каких-либо задач имею тягу создать максимально универсальное решение. В свободное от учебы время занимаюсь попытками написать что-либо практически применимое. Имею небольшой опыт в разработке сайтов. Умею программировать на следующих языках: c++, python, javascript.',
                'contacts': [
                    {'url': 'https://github.com/dburkov05', 'text': 'Github'},
                    {'url': 'mailto:dburkov05@bk.ru', 'text': 'Email'},
                    {'url': 'https://t.me/dburkov05', 'text': 'Telegram'},
                ],   
            },
    }
