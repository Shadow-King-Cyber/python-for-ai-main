"""Load environment variables from .env and print them."""
import os
from pathlib import Path

from dotenv import load_dotenv


def main() -> None:
    # Load the .env located next to this script (independent of the working directory)
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(env_path)

    api_key = os.environ.get("API_KEY")
    debug = os.environ.get("DEBUG")

    if api_key is None:
        print("API_KEY not found. Copy .env.example to .env and fill in your values.")
        return

    print(f"API Key: {api_key}")
    print(f"Debug mode: {debug}")


if __name__ == "__main__":
    main()
