import importlib
import importlib.metadata
import importlib.util
import sys

REQUIRED: dict[str, tuple[str, str]] = {
    "pandas": ("2.0.0", "Data manipulation ready"),
    "numpy": ("1.24.0", "Numerical computation ready"),
    "matplotlib": ("3.7.0", "Visualization ready"),
}

DATA_POINTS: int = 1000
OUTPUT_FILE: str = "matrix_analysis.png"


def is_installed(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def installed_version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def version_tuple(version: str) -> tuple[int, ...]:
    numbers: list[int] = []
    for piece in version.split(".")[:3]:
        digits: str = ""
        for char in piece:
            if not char.isdigit():
                break
            digits += char
        numbers.append(int(digits) if digits else 0)
    return tuple(numbers)


def check_dependencies() -> list[str]:
    missing: list[str] = []
    print("Checking dependencies:")
    for name, (_, description) in REQUIRED.items():
        if is_installed(name):
            version: str = installed_version(name)
            print(f"[OK] {name} ({version}) - {description}")
        else:
            print(f"[MISSING] {name} - required but not installed")
            missing.append(name)
    return missing


def show_install_help(missing: list[str]) -> None:
    print()
    print(f"ERROR: Missing dependencies: {', '.join(missing)}")
    print("The program cannot load without them.")
    print()
    print("Install them with pip:")
    print("  pip install -r requirements.txt")
    print("  python3 loading.py")
    print()
    print("Or install them with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def detect_manager() -> str:
    if sys.prefix == sys.base_prefix:
        return "global Python installation (pip, no isolation)"
    if "pypoetry" in sys.prefix:
        return "Poetry-managed virtual environment"
    return "virtual environment (likely pip + venv)"


def compare_versions() -> None:
    print()
    print("Package version comparison:")
    print(f"  {'package':<12}{'required':<12}{'installed':<12}status")
    for name, (minimum, _) in REQUIRED.items():
        current: str = installed_version(name)
        ok: bool = version_tuple(current) >= version_tuple(minimum)
        status: str = "OK" if ok else "TOO OLD"
        print(f"  {name:<12}{'>=' + minimum:<12}{current:<12}{status}")


def show_manager_differences() -> None:
    print()
    print("pip vs Poetry:")
    print("  pip    -> reads requirements.txt, installs into the active")
    print("            environment, no lock file, venv is up to you")
    print("  Poetry -> reads pyproject.toml, creates and manages its own")
    print("            virtual environment, pins exact versions in")
    print("            poetry.lock for reproducible installs")
    print(f"Current environment: {detect_manager()}")
    print(f"Python prefix: {sys.prefix}")


def run_analysis() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Analyzing Matrix data...")
    signal = np.random.normal(50, 10, DATA_POINTS)

    df = pd.DataFrame({"signal": signal})
    print(f"Processing {len(df)} data points...")
    anomalies = df[df["signal"] > 80]

    print("Generating visualization...")
    plt.plot(df["signal"])
    plt.savefig(OUTPUT_FILE)

    print()
    print("Analysis complete!")
    print(f"Mean signal: {df['signal'].mean():.2f}")
    print(f"Anomalies detected: {len(anomalies)}")
    print(f"Results saved to: {OUTPUT_FILE}")


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    missing: list[str] = check_dependencies()
    if missing:
        show_install_help(missing)
        show_manager_differences()
        sys.exit(1)
    print()
    run_analysis()
    compare_versions()
    show_manager_differences()


if __name__ == "__main__":
    main()
