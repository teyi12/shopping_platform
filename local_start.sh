echo "🔧 Chargement de l'environnement depuis .env"
export $(grep -v '^#' .env | xargs)

echo "🚀 Appliquer les migrations"
python manage.py migrate

echo "🧼 Collecte des fichiers statiques"
python manage.py collectstatic --noinput

echo "🌐 Lancement de Gunicorn sur le port $PORT"
exec gunicorn shopping_platform.wsgi:application --bind 127.0.0.1:$PORT