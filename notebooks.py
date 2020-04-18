from invoke import Collection, task

@task
def run(c, relative_path):
    c.run("jupyter nbconvert --ExecutePreprocessor.timeout=1000 --clear-output --execute {}".format(relative_path))
