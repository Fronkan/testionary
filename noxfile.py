import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["check", "test"]

LATEST_PYTHON = 14
OLDEST_PYTHON = 10
PYTHONS = list(range(OLDEST_PYTHON, LATEST_PYTHON + 1))


@nox.session(python=[f"3.{version}" for version in PYTHONS])
def test(session: nox.Session):
    session.install(".", "--group", "dev")
    session.run("pytest", "--doctest-glob=*.md", "--doctest-modules")


@nox.session(python=f"3.{OLDEST_PYTHON}")
def check(session: nox.Session):
    session.install("--group", "dev")
    session.run("ruff", "format", "--check")
    session.run("ruff", "check")


@nox.session(python=f"3.{OLDEST_PYTHON}")
def fix(session: nox.Session):
    session.install("--group", "dev")
    session.run("ruff", "format")
    session.run("ruff", "check", "--fix")
