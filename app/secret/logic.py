import os

import flask
import psycopg2
import psycopg2.extras

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

db = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname='outcognito',
                      cursor_factory=psycopg2.extras.NamedTupleCursor)

def filter_tweet():
    headers = flask.request.headers
    ip = headers.get('X-Forwarded-For') or headers.get('X-Real-IP') or flask.request.remote_addr
    ip = ip.split(',')[0].strip()  # XFF can have multiple IPs

    with db, db.cursor() as cursor:
        cursor.execute('select ip from bad_ips where ip=%s', (ip,))
        if cursor.fetchone():
            flask.abort(403)

    status = flask.request.values['status']
    if not (status.startswith('I just went to ') or status.startswith('I just typed ')):
        with db, db.cursor() as cursor:
            cursor.execute('insert into bad_ips (ip, status) values (%s, %s)', (ip, status))
        flask.abort(403)
