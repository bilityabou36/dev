
from pathlib import Path
import zipfile


def zip_directory(source_dir: str, output_zip: str) -> None:
    source_path = Path(source_dir)
    output_path = Path(output_zip)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in source_path.rglob("*"):
            if file_path.is_file():
                zipf.write(file_path, file_path.relative_to(source_path))


if __name__ == "__main__":
    zip_directory("app", "app_bundle.zip")
    print("Created app_bundle.zip")