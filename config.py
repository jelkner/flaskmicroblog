app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'microblog.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('MICROBLOG_SETTINGS', silent=True)
