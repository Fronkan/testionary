set dotenv-load := true

# Fix issue with folder permisions for scripts
set tempdir := "/tmp/"

# Set uv script runner
set unstable
set script-interpreter := ['uv', 'run', '--no-project', '--script']

@_:
	just --list
test:
	uvx nox

fix:
	uvx nox -s fix

publish: test && test_upload
	uv publish

test_upload:
	@just _is_latest_on_pypi
	@just _test_import_from_pypi

_test_import_from_pypi:
	@uv run --with testionary --no-project -- python -c "import testionary.basic as b; b.BasicTrackingDict()"

[script]
_is_latest_on_pypi:
	# /// script
	# requires-python = ">=3.11"
	# dependencies = [
	#   "requests",
	# ]
	# ///
	import sys
	import tomllib

	import requests

	resp = requests.get("https://pypi.org/simple/testionary", headers={"Accept": "application/vnd.pypi.simple.v1+json"})
	resp.raise_for_status()
	pypi_version = resp.json()["versions"][-1]
	with open("pyproject.toml", "rb") as f:
		proj = tomllib.load(f)
	local_version = proj["project"]["version"]
	print(f"{local_version=}", f"{pypi_version=}", sep="\n")
	if local_version == pypi_version:
		print("✔  Latest version on pypi matches local version")
	else:
		print(f"❌ Version mismatch: {local_version=} != {pyp_version=}")
		sys.exit(-1)
