# Releasing MCP Server to PyPI

This guide describes the steps to publish a new version of MCP Server to PyPI.

## 1. Bump Version

- Edit `pyproject.toml` and update the `version` field under `[project]` to the new release, e.g. `0.1.1`.
- Commit and tag the release:
  ```bash
  git add pyproject.toml
  git commit -m "Release v0.1.1"
  git tag v0.1.1
  git push origin main --tags
  ```

## 2. Build Distributions

Ensure you have `build` installed:
```bash
pip install build
```
Then build source and wheel:
```bash
python -m build
```

## 3. Publish with Twine

Install and use `twine` to securely upload:
```bash
pip install twine
twine upload dist/*
```

Your new version will be available on PyPI shortly.