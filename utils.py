import numpy as np
import json


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
                json.dump(data_source, f, sort_keys=True, cls=Encoder)
                print("Json data saved to "+filename+".")
                return True
        except BaseException as e:
            raise BaseException("Exception of save json: ", e)
