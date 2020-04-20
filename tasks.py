from invoke import Collection, task
import sys

@task
def run(c, relative_path):
    c.run("jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=1000 --execute {}".format(relative_path))
    sys.stdout.flush()
docs = Collection('docs')
docs.add_task(run)

@task
def start(c):
    c.run("honcho -f app/Procfile.dev start", pty=True)

app = Collection('app')
app.add_task(start)

ns = Collection()
ns.add_collection(docs)
ns.add_collection(app)
