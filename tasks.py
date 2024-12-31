#!/usr/bin/env python3

if not (
    (_i := __import__)("importlib.util").util.find_spec("swydd")
    or (_src := _i("pathlib").Path(__file__).parent / "swydd/__init__.py").is_file()
):  # noqa | https://github.com/daylinmorgan/swydd?tab=readme-ov-file#automagic-snippet
    _r = _i("urllib.request").request.urlopen("https://swydd.dayl.in/swydd.py")
    _src.parent.mkdir(exist_ok=True)
    _src.write_text(_r.read().decode())

from swydd import setenv, task, sub, cli, ctx

setenv(
    "HUGO_MODULE_REPLACEMENTS",
    "github.com/daylinmorgan/simple-recipe -> simple-recipe",
)

@task
def serve():
    """start dev build of site"""
    sub("hugo serve --buildDrafts --buildFuture --logLevel info " + " ".join(ctx.rest))


@task
def build():
    "build with local theme"
    sub("hugo" + " ".join(ctx.rest))

@task
def update():
    """update simple-recipe hash"""
    sub("hugo mod get")
    sub("hugo mod tidy")

cli("serve")
