import pytest
from main import biggestPath


class TestBiggestPath:
    @pytest.mark.parametrize("path, expected_result", [({'dir1': {}, 'dir2': ['file1'], 'dir3':
        {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}, "/dir3/dir5/dir6/dir7"),
                                              ({'dir1': ['file1', 'file1']}, "/"),
                                              ({"dir1": {}, "dir2": ['file1', 'file2']}, "/dir1")
                                              ])
    def test_path(self, path, expected_result):
        result_path = biggestPath(path)
        assert result_path == expected_result
