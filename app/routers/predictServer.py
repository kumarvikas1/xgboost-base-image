import os
import pickle

import numpy as np
import requests as req
from fastapi import APIRouter
from fastapi import HTTPException

from .monitor.timer import CustomMetrics

router = APIRouter()
custom_metrics = CustomMetrics("predict_service")
from typing import List
from pydantic import BaseModel


class Request(BaseModel):
    features: List[List[float]]


model_name = os.getenv("model_name")
loadedModel = req.get(
    f"http://model-service.ml-demo.svc.cluster.local/model-service/download-server/{model_name}").content
readyModel = pickle.loads(loadedModel)

# @profile
@router.get(path='/sampling-service/{model}/predict')
def predict1():
    try:
        with custom_metrics.model_latency_histogram.time():
            return readyModel.predict_proba(np.random.rand(4, 200)).tolist()
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail=f"error")


@router.post(path='/sampling-service/{model}/predict')
def predict1(request: Request, model):
    try:
        with custom_metrics.model_latency_histogram.time():
            return readyModel.predict_proba(np.array(request.features)).tolist()
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail=f"error")