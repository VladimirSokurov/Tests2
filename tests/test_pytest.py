from main import *

test_folder = ""
test_token = ""
uploader = YaUploader(test_token)


def test_get_all_doc_owners_names():
    result = uploader.create_folder(test_folder)
    assert 201 == result
