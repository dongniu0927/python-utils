import numpy as np
import json
import time
import pickle
import logging
import numpy.linalg as la  # 计算范数
import os
import sys

LOGGER = logging.getLogger(__name__)


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(Encoder, self).default(obj)


class Timer(object):
    """
    Record the consumed time when ran a code block.
    """
    def __init__(self, block_name, prefix="----->"):
        self.block_name = block_name
        self.prefix = prefix

    def __enter__(self):
        print(self.prefix+"Started '"+self.block_name+"' block...")
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = round(time.time() - self.time_start, 2)
        print(self.prefix+"Finished '"+self.block_name+"' block, time used:", str(elapsed_time)+"s.")


class Utils(object):

    @staticmethod
    def _print_verify_failed(hope, real):
        print("Verify failed: hope "+str(hope), ", but got "+str(real)+".")

    @staticmethod
    def verify_str(s):
        if not isinstance(s, str):
            Utils._print_verify_failed("str", type(s))
            raise BaseException("Must be a str type!")

    @staticmethod
    def verify_list(arr):
        if not isinstance(arr, list):
            Utils._print_verify_failed("list", type(arr))
            raise BaseException("Must be a list type!")

    @staticmethod
    def verify_ndarray(arr):
        if not isinstance(arr, np.ndarray):
            Utils._print_verify_failed("np.ndarray", type(arr))
            raise BaseException("Must be a np.ndarray type!")

    @staticmethod
    def verify_list_like(arr):
        if not isinstance(arr, (list, tuple, np.ndarray)):
            Utils._print_verify_failed("list, tuple, np.ndarray", type(arr))
            raise BaseException("Must be a list or tuple or np.ndarray!")

    @staticmethod
    def verify_equal_len(vec1, vec2):
        if len(vec1) != len(vec2):
            Utils._print_verify_failed("equal", len(vec1) + "," + len(vec2))
            raise BaseException("Must have same length!")

    @staticmethod
    def verify_len(vec, l):
        if len(vec) != l:
            Utils._print_verify_failed(l, len(vec))
            raise BaseException("Must have equal length as given!")

    @staticmethod
    def load_json(filename):
        try:
            with open(filename) as f:
                print("Success load "+filename+".")
                return json.load(f)
        except BaseException as e:
            raise BaseException("Exception of load json: ", e)

    @staticmethod
    def save_json(filename, data_source):
        try:
            with open(filename, "w") as f:
                json.dump(data_source, f, sort_keys=True,  separators=(',', ': '), cls=Encoder)
                print("Data saved to "+filename+".")
                return True
        except BaseException as e:
            raise BaseException("Exception of save json: ", e)

    @staticmethod
    def pickle(filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def unpickle(filename):
        try:
            with open(filename, "rb") as f:
                res = pickle.load(f)
            return res
        except IOError:
            LOGGER.debug('Unpickle error. Cannot find file: %s', filename)
            return None

    @staticmethod
    def normalize(v):
        Utils.verify_list(v)
        norm = la.norm(v, 2) + 0.00001
        v_new = []
        for i in range(len(v)):
            v_new.append(round(v[i] / norm, 4))
        return v_new

    @staticmethod
    def file_exist(file_path):
        return os.path.isfile(file_path)

    @staticmethod
    def get_working_path():
        return os.path.split(os.path.abspath(sys.argv[0]))[0]

    @staticmethod
    def list_files(dir_path):
        return os.listdir(dir_path)


class TestUtils(object):
    def test_timer(self):
        with Timer("Test"):
            pass


if __name__ == "__main__":
    test = TestUtils()
    test.test_timer()
