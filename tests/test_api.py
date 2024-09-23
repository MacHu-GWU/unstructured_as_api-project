# -*- coding: utf-8 -*-

from unstructured_as_api import api


def test():
    _ = api


if __name__ == "__main__":
    from unstructured_as_api.tests import run_cov_test

    run_cov_test(__file__, "unstructured_as_api.api", preview=False)
