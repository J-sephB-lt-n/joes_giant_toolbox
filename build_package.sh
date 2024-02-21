rm dist/*
python -m build
twine check dist/*
