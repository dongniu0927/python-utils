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