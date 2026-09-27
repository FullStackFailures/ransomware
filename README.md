# SystemPrank — Ransomware UI Simulation

A small Python/Kivy/Tkinter project that **simulates a ransomware-style lock screen for cybersecurity education and demonstrations**.

> ⚠️ **LAB USE ONLY**
>
> Run this project only in an isolated test environment, such as a disposable VM/emulator. Do not deploy it against systems or data you do not own or have explicit permission to test.

## What it does

- Displays a fullscreen "system breach/encryption" interface.
- Shows fake file paths and simulated encryption progress.
- Requires a password to dismiss the demo.
- Includes a desktop Tkinter version: `ransomware/ransomware.py`
- Includes a Kivy version intended for Android packaging: `ransomware/SystemPrank/`
- The supplied source does **not** implement actual file encryption or data destruction.

## Project structure

```text
ransomware/
├── ransomware.py
└── SystemPrank/
    ├── main.py
    ├── ui.kv
    ├── buildozer.spec
    ├── main.spec
    └── requirements.txt
```

The ZIP also contains generated `.venv`, `.buildozer`, `build`, and `dist` artifacts. These are local build artifacts and should normally be removed before committing the project to GitHub.

## Desktop demo

The desktop implementation uses Python's standard-library `tkinter`, so it does not need a Python package for the Tkinter version.

```bash
cd ransomware
python ransomware.py
```

Use an isolated VM for testing.

The password is hard-coded in the supplied demo source. **Do not treat it as a secret.**

## Kivy setup

The Android-oriented project uses Kivy 2.3.1 and Buildozer 1.6.0 in the supplied development environment.

Create a virtual environment:

```bash
cd ransomware/SystemPrank
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Windows, Buildozer is normally used through WSL/Linux rather than native PowerShell.

## Run the Kivy demo

```bash
cd ransomware/SystemPrank
python main.py
```

This requires Kivy and a working graphical environment.

## Build Android APK

Buildozer is intended for Linux/WSL environments.

```bash
cd ransomware/SystemPrank
source .venv/bin/activate

buildozer android debug
```

The APK is normally produced under:

```text
bin/
```

For a clean rebuild:

```bash
buildozer android clean
buildozer android debug
```

## Security / responsible use

Do not add persistence, privilege escalation, real file encryption, credential theft, evasion, destructive behavior, or unauthorized deployment to this project.

The repository operator and users are responsible for ensuring that any demonstration, modification, distribution, and testing is lawful and authorized.

## License

This project is released under the **MIT License**. See [`LICENSE`](LICENSE).
