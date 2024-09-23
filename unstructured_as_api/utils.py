# -*- coding: utf-8 -*-

import base64


def bytes_to_str(b: bytes) -> str:
    return base64.b64encode(b).decode("utf-8")


def str_to_bytes(s: str) -> bytes:
    return base64.b64decode(s.encode("utf-8"))
