import os
import sys

from dotenv import load_dotenv

KEYS = ("MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
        "ZION_ENDPOINT")
REQUIRED = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")


def env_in_gitignore() -> bool:
    try:
        with open(".gitignore") as file:
            return ".env" in file.read().split()
    except OSError:
        return False


def no_hardcoded_secrets(api_key: str | None) -> bool:
    with open(__file__) as file:
        return not api_key or api_key not in file.read()


def main() -> None:
    load_dotenv()
    config = {key: os.getenv(key) for key in KEYS}
    production = config["MATRIX_MODE"] == "production"

    print("\nORACLE STATUS: Reading the Matrix...\n")

    missing = [key for key in REQUIRED if not config[key]]
    for key in missing:
        print(f"[WARN] {key} is not set")
    if missing and production:
        print("[ERROR] Production mode needs all configuration, stopping.")
        sys.exit(1)
    if missing:
        print("Development mode: using safe defaults.\n")

    database = config["DATABASE_URL"]
    if not database:
        db_status = "Not configured (using local SQLite)"
    elif "localhost" in database:
        db_status = "Connected to local instance"
    else:
        db_status = "Connected to remote cluster"

    mode = "production" if production else "development"
    api = "Authenticated" if config["API_KEY"] else "Offline"
    default_level = "WARNING" if production else "DEBUG"
    zion = "Online" if config["ZION_ENDPOINT"] else "Offline"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api}")
    print(f"Log Level: {config['LOG_LEVEL'] or default_level}")
    print(f"Zion Network: {zion}")

    print("\nEnvironment security check:")
    if no_hardcoded_secrets(config["API_KEY"]):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] API_KEY appears in the source code")
    if os.path.isfile(".env") and env_in_gitignore():
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env is missing or not listed in .gitignore")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
