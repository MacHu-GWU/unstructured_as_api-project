# -*- coding: utf-8 -*-

import typing as T
import io

from pydantic import Field

from unstructured.partition.pdf import partition_pdf

from ..model import BaseResponse

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3.client import S3Client


class BasePartitionResponse(BaseResponse):
    elements: T.List[T.Dict[str, T.Any]] = Field(default_factory=list)


class PartitionPdfSyncResponse(BasePartitionResponse):
    pass


def part_pdf(
    content: bytes,
) -> BasePartitionResponse:
    elements = partition_pdf(file=io.BytesIO(content))
    res = PartitionPdfSyncResponse(elements=[element.to_dict() for element in elements])
    return res
