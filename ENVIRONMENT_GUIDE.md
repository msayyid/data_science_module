# Environment Guide - Multi Device Workflow

This project uses a local virtual environment (.venv) and a shared `requirements.txt` file to keep dependencies consistent across devices (Windows and macOS).

---

## First Time Setup (On Any Device)

After cloning or pulling the project:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

Mac:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

## If You Install a New Library

If you install something new:

```bash
pip install package_name
```

You MUST update the requirements file:

```bash
pip freeze > requirements.txt
```

Then commit and push:

```bash
git add requirements.txt
git commit -m "Add package_name"
git push
```

This ensures other devices can install the same dependencies.

---

## On the Other Device

After pulling changes:

```bash
git pull
pip install -r requirements.txt
```

---

## Important Rules

1. Never commit the `.venv` folder.
2. Always commit `requirements.txt` after installing a new package.
3. If environment breaks, delete `.venv` and recreate it.

---

## If Environment Gets Corrupted

Delete the environment:

Windows:

```bash
Remove-Item -Recurse -Force .\.venv
```

Mac:

```bash
rm -rf .venv
```

Then recreate it using the First Time Setup steps.

---

This keeps Windows and macOS environments identical and prevents dependency conflicts.
