# プロジェクトを作成する
`docker compose run --rm web django-admin startproject config .`
# アプリを１つ作成する(ここではtodoアプリ)
`docker compose run --rm web python manage.py startapp todo`
# 起動する
`docker compose up`
