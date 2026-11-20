def greet(name: str) -> str:
    """Return a friendly greeting."""
    name = name.strip()
    return f"Hello, {name or 'world'}!"


def main() -> None:
    print(greet("Thoriso"))


if __name__ == "__main__":
    main()
