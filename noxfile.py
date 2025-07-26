import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["check", "test"]

LATEST_PYTHON = 14
OLDEST_PYTHON = 10
PYTHONS = list(range(OLDEST_PYTHON, LATEST_PYTHON + 1))


@nox.session(python=[f"3.{version}" for version in PYTHONS])
def test(session):
    session.install(".", "--group", "dev")
    session.run("pytest")


@nox.session(python="3.10")
def check(session):
    session.install("--group", "dev")
    session.run("ruff", "format", "--check")
    session.run("ruff", "check")


@nox.session(python="3.10")
def fix(session):
    session.install("--group", "dev")
    session.run("ruff", "format")
    session.run("ruff", "check", "--fix")
