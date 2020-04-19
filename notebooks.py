from invoke import Collection, task

@task
def run(c, relative_path):
    c.run("jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=1000 --execute {}".format(relative_path))
