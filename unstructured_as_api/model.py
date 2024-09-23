# -*- coding: utf-8 -*-

from pydantic import BaseModel


class BaseResponse(BaseModel):
    pass


class BaseRequest(BaseModel):
    def send(self, **kwargs):
        raise NotImplementedError
