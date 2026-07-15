from django.shortcuts import render 


def home(request):
    context = {
        'my_name': 'Дмитрий',
        'age': '34',
        'about1': 'дочки',
        'about2': 'любимой жены'
    }
    return render(request, 'frontend/index.html', context)

def text(request):
    context = {
        'my_name': 'Дмитрий',
        'status1': 'Папочка',
        'status2': 'Дорогой муж',
        'status3': '',
        'pod1': 'Дорогой муж и папочка мы поздравляем тебя с днем рождения желаем главного счастья и доровья! Мы тебя очень любим!',
        'pod2': 'я поздравляю тебя с днем рождения! Желаю оставаться таким же здоровым, сильным и чтобы у тебя исполнились все мечты! Я тебя очень люблю ❤️',
        'pod3': 'я поздравляю тебя с днем рождения! Желаю счастья, веселья и крепкого здоровья! Люблю тебя ❤️',
        'about1': 'дочки',
        'about2': 'любимой жены',
        'color': 'blue'
    }
    return render(request, 'frontend/text.html', context)

def photo(request):
    context = {
        'photo1': 'photik1.png',
        'photo2': 'photik2.png',
        'photo3': 'photik3.png',
        'photo4': 'photik4.png',
        'photo5': 'photik5.png',
        'photo6': '',
        'photo7': '',
        'photo8': ''
}
    return render(request, 'frontend/photo.html', context)
def present(request):
    context = {
        'present1': 'Уктус, Зимняя улица, 27/3, 620076, Екатеринбург, Уктус м-н, Чкаловский район',
        'present2': 'Открытка в секретном месте',
        'present3': '',
        'about1': 'дочки',
        'about2': 'любимой жены'
    }
    return render(request, 'frontend/present.html', context)
