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

## ⚠️ Disclaimer

This repository contains **ransomware-style software intended for cybersecurity education, research, demonstrations, and authorized security testing in controlled environments**.

The original repository is maintained by **FullStackFailures**:

https://github.com/FullStackFailures

The authors and maintainers **do not endorse, encourage, or authorize** the use of this software for malicious, illegal, unauthorized, or harmful activities.

By downloading, using, modifying, deploying, or distributing this repository, you acknowledge that **you are solely responsible for your actions and for complying with all applicable laws, regulations, organizational policies, and third-party terms of service**.

The repository owner and contributors shall **not be held responsible for misuse, damage, data loss, unauthorized access, disruption, or any other consequences resulting from the use or modification of this software, to the extent permitted by applicable law**.

Use this project only on systems, devices, networks, and data for which you have explicit authorization.

**For educational and ethical hacking purposes only.**

## License

This project is released under the **MIT License**. See [`LICENSE`](LICENSE).
