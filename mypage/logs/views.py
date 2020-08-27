from django.shortcuts import render
from logs.models import Comment
from logs.forms import CommentForm
from django.http import HttpResponseRedirect

def get_name(request):

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()

            # Редирект на ту же страницу
            return HttpResponseRedirect(request.path_info)

    else:
    # метод GET

        form = CommentForm()

        # Получение всех имен из БД.
        names = Comment.objects.all().order_by("-date_added")

    # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
    return render(request, 'logs/comments.html', {'form': form, 'names': names})
