import zipfile
import pathlib


def make_zip(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "app.zip")
    with zipfile.ZipFile(dest_path, "w") as zip:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    print("Hi from zipfile")


