# Install
1. `pip install -r requirements/dev.txt`
2. `foreman run python manage.py clean_db`
3. `foreman run python manage.py runserver`

# Deploy

## Heroku
```sh
#!/usr/bin/env fish
heroku plugins:install git://github.com/joelvh/heroku-config.git
heroku addons:add newrelic:standard
heroku addons:add redistogo
heroku addons:add memcachier:dev
heroku addons:add heroku-postgresql:dev
heroku labs:enable user-env-compile #enabled so that collectstatic has access to amazon ec2 key
heroku config:push -o --filename config/env/common.env
heroku config:push -o --filename config/env/prod.env
heroku pg:promote (heroku pg | grep '^===' | sed 's/^=== //g')
git push heroku master
heroku run 'python manage.py clean_db'
```

## Travis
```sh
#!/usr/bin/env fish
gem install travis
echo '# do not modify this file. it is generated from configs/travis/base.travis.yml' > '.travis.yml'
cat configs/travis/base.travis.yml >> '.travis.yml'
for line in (cat configs/env/common.env configs/env/testing.env);
    echo '  '(travis encrypt saulshanabrook/django-canadanewyork $line | grep '  secure') >> '.travis.yml';
end
echo '  '(travis encrypt saulshanabrook/django-canadanewyork HEROKU_API_KEY=(heroku auth:token) | grep '  secure') >> '.travis.yml'
```

# Schema

## Migrate

```sh
#!/usr/bin/env fish
for app in (python manage.py syncdb | grep - | sed 's/ - //g');
    python manage.py schemamigration $app --auto;
end
```
## Wipe Migrations

```sh
#!/usr/bin/env fish
rm -r {apps,libs}/*/migrations
```

## Initial Migrations
```sh
#!/usr/bin/env fish
for app in (python manage.py syncdb | grep '^ . apps\|libs' | sed 's/ > //g' | sed 's/ - //g');
    python manage.py schemamigration $app --initial;
end
```