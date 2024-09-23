# -*- coding: utf-8 -*-

import requests
from pathlib import Path
from boto_session_manager import BotoSesManager
from s3pathlib import S3Path, context
from unstructured_as_api.utils import bytes_to_str
from rich import print as rprint

dir_here = Path.cwd().absolute()
bsm = BotoSesManager(profile_name="bmt_app_dev_us_east_1")
context.attach_boto_session(bsm.boto_ses)

bucket = f"{bsm.aws_account_alias}-{bsm.aws_region}-data"
s3dir_root = S3Path(f"s3://{bucket}/projects/unstructured_as_api/")
s3dir_input = s3dir_root.joinpath("input/")
s3dir_output = s3dir_root.joinpath("output/")

s3path_in = s3dir_input.joinpath("f1040.pdf")
path = dir_here.joinpath("f1040.pdf")
s3path_in.write_bytes(path.read_bytes())

domain = "http://127.0.0.1:8000"

res = requests.post(
    f"{domain}/part_pdf/",
    json={
        "b64_content": bytes_to_str(path.read_bytes()),
    }
)
rprint(res.json()["elements"][:3])

res = requests.post(
    f"{domain}/start_part_pdf/",
    json={
        "s3uri_in": s3path_in.uri,
        "s3uri_out": s3dir_output.uri,
    }
)
res_data = res.json()
job_id = res_data["job_id"]
print(res_data)

res = requests.post(
    f"{domain}/get_part_pdf/",
    json={
        "job_id": job_id,
    }
)
res_data = res.json()
res_data["elements"] = res_data["elements"][:3]
rprint(res_data)
