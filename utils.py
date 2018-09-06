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
    def print_verify_failed(msg):
        print("Verify failed msg: ", msg)

    @staticmethod
    def verify_str(s):
        if not isinstance(s, str):
            Utils.print_verify_failed(type(s))
            raise BaseException("Must be a str type!")

    @staticmethod
    def verify_list(arr):
        if not isinstance(arr, list):
            Utils.print_verify_failed(type(arr))
            raise BaseException("Must be a list type!")

    @staticmethod
    def verify_list_like(arr):
        if not isinstance(arr, (list, tuple, np.ndarray)):
            Utils.print_verify_failed(type(arr))
            raise BaseException("Must be a list like (include:list, tuple, np.ndarray)!")

    @staticmethod
    def verify_ndarray(arr):
        if not isinstance(arr, np.ndarray):
            Utils.print_verify_failed(type(arr))
            raise BaseException("Must be a np.ndarray type!")

    @staticmethod
    def verify_ndarray_list(arrs):
        Utils.verify_list(arrs)
        for arr in arrs:
            Utils.verify_ndarray(arr)

    @staticmethod
    def verify_equal_len(vec1, vec2):
        if len(vec1) != len(vec2):
            Utils.print_verify_failed("length are " + str(len(vec1)) + " and "+str(len(vec2)))
            raise BaseException("Must have same length!")

    @staticmethod
    def verify_len(vec, l):
        if len(vec) != l:
            Utils.print_verify_failed("wrong length:"+str(len(vec)))
            raise BaseException("Vec length wrong!")

    @staticmethod
    def save_json(filename, data_source):
        try:
            with open(filename, "w") as f:
                json.dump(data_source, f, sort_keys=True,  separators=(',', ': '))  # indent=4
                print("Data saved to "+filename)
                return True
        except BaseException as e:
            print("Wrong data: ", data_source)
            raise BaseException("Exception of save json: ", e)

    @staticmethod
    def load_json(filename):
        try:
            with open(filename) as f:
                print("Success load "+filename)
                return json.load(f)
        except BaseException as e:
            print("Exception of load json: ", e)
            return False
