# プロジェクトを作成する(最後の`.`を忘れずに)
`docker compose run --rm web django-admin startproject config .`
# アプリを１つ作成する(ここではtodoアプリ)
`docker compose run --rm web python manage.py startapp todo`
# 起動する
`docker compose up`
# ブラウザで開く　
http://localhost:4989

# makemigrationする時
`docker compose run --rm web python manage.py makemigrations`

# migrateする時
`docker compose run --rm web python manage.py migrate`

# 管理サイトにログインできるようにする時
`docker compose run --rm web python manage.py createsuperuser`
