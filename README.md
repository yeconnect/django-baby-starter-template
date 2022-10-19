# ビルドする
`docker compose build`

# DBにmigrateする
`docker compose run --rm web python manage.py migrate`

# サンプルデータをDBに投入する
`docker compose run --rm web python manage.py loaddata todo/fixtures/todos-data.json`

# サーバーを起動する
`docker compose up`

# todo一覧APIを見る
http://localhost:8000/todo

# APIのスキーマをUIで見る。(OpenAPI)
http://localhost:8000/docs