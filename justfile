set positional-arguments

VERSION := `uv run scripts/get_version.py modrinth_api_wrapper/__init__.py`

test:
  uv run --with pytest python -m pytest tests
  just clean

build:
  uv build

release:
  @echo 'Tagging v{{VERSION}}...'
  git tag "v{{VERSION}}"
  @echo 'Push to GitHub to trigger publish process...'
  git push --tags

publish:
  uv build
  uv publish
  git push --tags
  just clean-builds

clean-builds:
  rm -rf build/
  rm -rf dist/

ci-install:
  uv sync --all-extras --dev

clean:
  rm -rf .pytest_cache/
  rm -rf .mypy_cache/
