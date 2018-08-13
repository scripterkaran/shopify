source venv/bin/activate
cd webapp
yarn run build
cd ..
python manage.py collectstatic --noinput
cat webapp/dist/index.html >> templates/shop-index-spa.html