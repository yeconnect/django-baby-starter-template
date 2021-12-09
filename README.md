# プロジェクトを作成する
`docker compose run --rm web django-admin startproject config .`
# アプリを１つ作成する(ここではtodoアプリ)
`docker compose run --rm web python manage.py startapp todo`
# 起動する
`docker compose up`

# DB設計を決定する(makemigrations)
`docker compose run --rm web python manage.py makemigrations`

# DBに反映する(migrate)
`docker compose run --rm web python manage.py migrate`

# 管理ユーザの追加(createsuperuser)
`docker compose run --rm web python manage.py createsuperuser`