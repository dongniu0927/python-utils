import numpy as np


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