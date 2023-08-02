[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]

<h1>Django Blog</h1>
<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

What is Django Blog?
-------------

**Project created for educational purposes!**

<br>

Service developed in Python 4.11 with [Django 4.2.3](https://www.djangoproject.com/) framework, following PEP 8 regulations such as ([Flake8 6.0](https://github.com/pycqa/flake8/blob/main/docs/source/index.rst) and [MyPy 1.4](https://github.com/python/mypy)). Front-End made with HTML5, CSS3 and JavaScript. [Docker](https://www.docker.com/) container was used to run the local server and the Postgresql server.

The blog has a customized administrative area of ​​Django itself, protected with loggin and [Django-Axes 6.0](https://github.com/jazzband/django-axes/tree/master) to avoid forced entry by malicious agents.

Through the administrative area it is possible to make posts in HTML with the help of [Django-Summernote 0.8](https://github.com/summernote/django-summernote), upload post cover images and post content images with the help of [Pillow 9.5](https://pypi.org/project/Pillow/) for automatic resizing of the images, define which posts will appear publicly, register and choose categories and tags for publications.
As an administrator, you can configure elements of the site itself, such as header, footer, menu and shortcut links. Add and remove pages that are content apart from the blog.
<br><br>

`(PT-BR) Serviço desenvolvido em python 4.11 com framework django 4.2, seguindo normativas da PEP 8 como (flake8 6.0 e mypy 1.4). Front-End foi feito com HTML5, CSS3 e JavaScript. Utilizou-se conteiner Docker para rodar o servidor local e o servidor Postgresql.
O blog possui área administrativa customizada do próprio django, protegida com loggin e Django-Axes 6.0 para evitar entrada forçada de agentes maliciosos.
Pela área administrativa é possível fazer posts em HTML com auxilio do Django-Summernote 0.8, upload de imagens de capa do posts e imagens de conteúdo do post com auxilio do Pillow 9.5 para redimensionamento automatico das imagens, definir quais postagens irão aparecer publicamente, cadastrar e escolher categorias e tags para as publicações.
Como adminitrador, pode-se configurar elementos do próprio site, como cabeçalho, rodapé, menu e links de atalhos. Adicionar e remover páginas que são conteúdos a parte do blog.`


Quick start
-----------

To access the project's localhost, install Docker and download the complete project.

Afterwards, rename the /dotenv_files/.env-example file to /dotenv_files/.env and modify the data contained within the file. The SECRET_KEY can be obtained by the command:

```
python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
```

Open the project folder in VisualStudio Code and run docker-compose in the root folder:

```
docker-compose up --build
```

Afterwards, with docker running and in a new terminal, create the superuser to access the django admin page:

```
docker-compose run --rm djangoapp python manage.py createsuperuser
```

After that, you will have access to the blog's admin page at 127.0.0.1:8000/admin. The blog will be running at address 127.0.0.1:8000

To stop the server just press Ctrl + C in the Docker terminal.

After creating the docker image, just type the command below to start the server again:

```
docker-compose up
```

<br><br>

(PT-BR) Como usar
-----------

`Para acesso em localhost do projeto deve-se instalar o Docker e baixar o projeto completo.
Após, renomeie o arquivo /dotenv_files/.env-example para /dotenv_files/.env e modifique os dados contidos dentro do aquivo. A SECRET_KEY pode ser conseguida pela comando:`

```
python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
``` 
`Abra a pasta do projeto no VisualStudio Code e execute o docker-compose na pasta raiz:`
```
docker-compose up --build
```
`Após, com o docker rodando e em um novo terminal, crie o super-usuário para acessar a pagina de admin do django: `
```
docker-compose run --rm djangoapp python manage.py createsuperuser
```
`Após isso você terá acesso á pagina admin do blog pelo endereço 127.0.0.1:8000/admin. O blog irá estar rodando no endereço 127.0.0.1:8000`
`Para parar o servidor basta presionar Ctrl + C no terminal Docker.
Após criada a imagem docker, basta digitar o comando abaixo para iniciar o servidor novamente:`

```
docker-compose up
```
<br><br>


Immages
-----------
<br>

## BLOG PAGE AND ADMINISTRATION


https://github.com/RuanGemmer/Blog/assets/130599502/bf826949-44c8-4a5c-b649-2c16c060dd62


<br>

## ADMIN PAGE
<h4>Login screen</h4>
<div class="align-center">
  <a href="https://freeimage.host/i/HZSnUMX"><img src="https://iili.io/HZSnUMX.md.png" alt="HZSnUMX.md.png" border="0"></a>
</div>

<h4>Admin Home</h4>
<div class="align-center">
  <a href="https://freeimage.host/i/HZSn4Fs"><img src="https://iili.io/HZSn4Fs.md.png" alt="HZSn4Fs.md.png" border="0"></a>
</div>

<h4>General Site Setup</h4>
<div class="align-center">
  <a href="https://freeimage.host/i/HZSnPSf"><img src="https://iili.io/HZSnPSf.md.png" alt="HZSnPSf.md.png" border="0"></a>
</div>

<h4>Category maintenance</h4>
<div class="align-center">
  <a href="https://freeimage.host/i/HZSngPn"><img src="https://iili.io/HZSngPn.md.png" alt="HZSngPn.md.png" border="0"></a>
</div>

<h4>Page maintenance</h4>
<div class="align-center">
  <a href="https://freeimage.host/i/HZSn6cG"><img src="https://iili.io/HZSn6cG.md.png" alt="HZSn6cG.md.png" border="0"></a>
</div>

<h4>Post maintenance</h4>
<div class="align-center">
  <a href="https://freeimage.host/i/HZSns94"><img src="https://iili.io/HZSns94.md.png" alt="HZSns94.md.png" border="0"></a>
</div>




 <!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RuanGemmer/Blog.svg?style=for-the-badge
[contributors-url]: https://github.com/RuanGemmer/Blog/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RuanGemmer/Blog.svg?style=for-the-badge
[forks-url]: https://github.com/RuanGemmer/Blog/network/members
[stars-shield]: https://img.shields.io/github/stars/RuanGemmer/Blog.svg?style=for-the-badge
[stars-url]: https://github.com/RuanGemmer/Blog/stargazers
