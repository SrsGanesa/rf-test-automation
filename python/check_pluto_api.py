"""
Software-only verification of the pyadi-iio Pluto interface.

This script does NOT connect to an ADALM-Pluto.
It only verifies that the pyadi-iio Pluto class can be imported
and inspected from the project Python environment.
"""

import inspect
import adi


def main() -> None:
    print("=" * 60)
    print("RF TEST AUTOMATION - PYADI-IIO PLUTO API CHECK")
    print("=" * 60)

    print(f"pyadi-iio version : {adi.__version__}")
    print(f"Pluto class      : {adi.Pluto}")
    print(f"Module           : {adi.Pluto.__module__}")

    print("\nConstructor signature:")
    try:
        print(inspect.signature(adi.Pluto))
    except (TypeError, ValueError):
        print("Signature could not be determined.")

    print("\nSelected public attributes/methods:")

    public_members = [
        name
        for name in dir(adi.Pluto)
        if not name.startswith("_")
    ]

    for name in public_members:
        print(f"  - {name}")

    print("\nNo hardware connection was attempted.")
    print("API import check completed successfully.")


if __name__ == "__main__":
    main()
    