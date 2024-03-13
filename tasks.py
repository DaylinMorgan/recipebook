#!/usr/bin/env python3
# # https://github.com/daylinmorgan/swydd?tab=readme-ov-file#automagic-snippet
# fmt: off
if not (src := __import__("pathlib").Path(__file__).parent / "swydd/__init__.py").is_file(): # noqa
    try: __import__("swydd") # noqa
    except ImportError:
        import sys; from urllib.request import urlopen; from urllib.error import URLError # noqa
        try: r = urlopen("https://raw.githubusercontent.com/daylinmorgan/swydd/main/src/swydd/__init__.py") # noqa
        except URLError as e: sys.exit(f"error fetching swydd: {e}\n") # noqa
        src.parent.mkdir(exist_ok=True); src.write_text(r.read().decode("utf-8")); # noqa
# fmt: on

import swydd as s

s.define_env("HUGO_MODULE_REPLACEMENTS","github.com/daylinmorgan/simple-recipe -> simple-recipe")

@s.task
def serve():
    """start dev build of site"""
    s.sh("hugo serve --buildDrafts --buildFuture --logLevel info")


@s.task
def build():
    "build with local theme"
    s.sh("hugo")

s.cli()
