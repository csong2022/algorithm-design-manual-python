import filecmp
import os
import os.path as path
from contextlib import redirect_stdout


def execute(testcase, input_filename, output_filename):
    """
    Test engine reply test case, and compare output with expected.

    :param testcase: test case to be executed.
    :param input_filename: input file name.
    :param output_filename: expected output file name.
    :return: true if output matches expected, otherwise false.
    """
    root_dir = _root_dir()
    out_dir = path.join(root_dir, "out")
    if not path.exists(out_dir):
        os.mkdir(out_dir)

    data_dir = path.join(root_dir, "datafiles")

    output_path = path.join(out_dir, output_filename)
    if path.exists(output_path):
        os.remove(output_path)

    with open(output_path, 'w') as output_file, redirect_stdout(output_file):
        if input_filename is not None:
            input_path = path.join(data_dir, input_filename)
            with open(input_path, 'r') as input_file:
                testcase.process(input_file)
        else:
            testcase.process()

    expected_path = path.join(data_dir, output_filename)
    return filecmp.cmp(output_path, expected_path, False)


def _root_dir():
    return path.join(path.split(__file__)[0], '../../..')
