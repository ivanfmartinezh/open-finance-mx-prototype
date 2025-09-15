from __future__ import annotations

from src.api.belvo_client import get_belvo_client


def main() -> None:
    client = get_belvo_client()
    print("Conexión creada con Belvo Sandbox")
    print("Listando instituciones (primeras 5):")
    institutions = client.Institutions.list()
    for i, inst in enumerate(institutions):
        print(f"  - {inst['name']} ({inst['type']})")
        if i >= 4:
            break


if __name__ == "__main__":
    main()
