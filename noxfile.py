import nox

nox.options.default_venv_backend = "uv"

@nox.session(python=[f"3.{version}" for version in range(10,15)])
def test(session):
    session.install(".", "--group", "dev")
    session.run("pytest")
