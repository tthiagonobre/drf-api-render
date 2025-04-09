import os
import django
from django.contrib.auth import get_user_model

# Executa só se a variável de ambiente CREATE_SUPERUSER estiver como 'true'
if os.environ.get('CREATE_SUPERUSER') == 'true':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')  # ajuste o nome
    django.setup()

    User = get_user_model()

    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'tthiagonobre')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'tcardosonobre@gmail.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'MLJXHAMt_7')

    if not User.objects.filter(username=username).exists():
        print("Criando superusuário...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("Superusuário já existe.")
