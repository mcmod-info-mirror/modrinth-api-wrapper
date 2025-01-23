set positional-arguments

VERSION := `uv run scripts/get_version.py modrinth_api_wrapper/__init__.py`

test:
  uv run pytest .\tests\
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