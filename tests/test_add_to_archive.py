import os
import shutil
from zipfile import ZipFile, ZIP_STORED

from conftest import TMP_DIR, TEST_DATA_DIR, CURRENT_DIR

files_dir = os.listdir(TEST_DATA_DIR)


def test_add_files_to_zip_via_shutil():
    shutil._make_zipfile(base_name=f'{TMP_DIR}\hello', base_dir=TEST_DATA_DIR)
    assert os.path.isfile(f'{TMP_DIR}\hello.zip')

def test_add_files_to_zip_via_zipfile():
    if os.path.isfile(f'{TMP_DIR}\hello.zip'):
        shutil.rmtree(TMP_DIR)

    os.mkdir(f'{CURRENT_DIR}\\resources')

    with ZipFile(f'{TMP_DIR}\hello.zip', mode='w', compression=ZIP_STORED) as zip_file:
        for file in files_dir:
            add_file = os.path.join(TEST_DATA_DIR, file)
            zip_file.write(add_file)
    assert os.path.isfile(f'{TMP_DIR}\hello.zip')