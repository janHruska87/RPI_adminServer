# scripts/export_openapi.py

def main():
    from app.main import app2
    import json

    with open("openapi.json", "w") as f:
        json.dump(app2.openapi(), f, indent=2)

    print("✅ OpenAPI specifikace byla exportována do openapi.json")
