# -*- coding: utf-8 -*-

import json
import uuid
from boto_session_manager import BotoSesManager
from pydantic import BaseModel

from fastapi import FastAPI, BackgroundTasks
from s3pathlib import S3Path

from unstructured_as_api.utils import str_to_bytes
from unstructured_as_api.meth.partition import (
    part_pdf,
)

app = FastAPI()

bsm = BotoSesManager(profile_name="bmt_app_dev_us_east_1")
bucket = f"{bsm.aws_account_alias}-{bsm.aws_region}-data"
s3dir_root = S3Path(f"s3://{bucket}/projects/unstructured_as_api/")
s3dir_jobs = s3dir_root.joinpath("jobs").to_dir()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class PartitionPdfRequest(BaseModel):
    b64_content: str


@app.post(
    "/part_pdf/",
)
async def partition_pdf(
    req: PartitionPdfRequest,
):
    # print("--- start: 'partition_pdf' ---")
    res = part_pdf(content=str_to_bytes(req.b64_content))
    return res.dict()


class StartPartitionPdfRequest(BaseModel):
    s3uri_in: str
    s3uri_out: str


async def process_start_partition_pdf_task(
    job_id: str,
    s3uri_in: str,
    s3uri_out: str,
):
    s3dir_out = S3Path(s3uri_out)
    s3path_out = s3dir_out.joinpath(job_id, "output.json")
    s3path_status = s3dir_out.joinpath(job_id, "status.txt")
    try:
        res = part_pdf(content=S3Path(s3uri_in).read_bytes(bsm=bsm))
        s3path_out.write_text(res.json(), content_type="application/json", bsm=bsm)
        s3path_status.write_text("SUCCEEDED", content_type="text/plain", bsm=bsm)
    except Exception as e:
        s3path_status.write_text("FAILED", content_type="text/plain", bsm=bsm)
        raise e


@app.post(
    "/start_part_pdf/",
)
async def start_partition_pdf(
    req: StartPartitionPdfRequest,
    background_tasks: BackgroundTasks,
):
    # print("--- start: 'start_partition_pdf' ---")
    job_id = str(uuid.uuid4())
    s3path_job = s3dir_jobs.joinpath(f"{job_id}.json")
    # print(f"job metadata: {s3path_job.uri}")
    s3path_job.write_text(req.json(), content_type="application/json", bsm=bsm)

    s3dir_out = S3Path(req.s3uri_out)
    s3path_status = s3dir_out.joinpath(job_id, "status.txt")
    s3path_status.write_text("RUNNING", content_type="text/plain", bsm=bsm)

    background_tasks.add_task(
        process_start_partition_pdf_task,
        job_id,
        req.s3uri_in,
        req.s3uri_out,
    )
    return {"job_id": job_id}


class GetPartitionPdfRequest(BaseModel):
    job_id: str


@app.post(
    "/get_part_pdf/",
)
async def get_partition_pdf(
    req: GetPartitionPdfRequest,
):
    # print("--- start: 'get_partition_pdf' ---")
    s3path_job = s3dir_jobs.joinpath(f"{req.job_id}.json")
    # print(f"job metadata: {s3path_job.uri}")
    data = json.loads(s3path_job.read_text(bsm=bsm))
    s3dir_out = S3Path(data["s3uri_out"])
    s3path_out = s3dir_out.joinpath(req.job_id, "output.json")
    s3path_status = s3dir_out.joinpath(req.job_id, "status.txt")
    status = s3path_status.read_text(bsm=bsm)
    res = {"status": status}
    if status == "SUCCEEDED":
        res["elements"] = json.loads(s3path_out.read_text(bsm=bsm))["elements"]
    return res
