# 初期の構築

## React側のcreate-react-appをする
`docker compose run --rm react sh -c "npm install -g create-react-app && create-react-app app"`

## Django側のstartprojectをする
`docker compose run --rm django django-admin startproject config .`