set dotenv-load := true

test:
	uvx nox

fix:
	uvx nox -s fix

publish: test
	uv publish

