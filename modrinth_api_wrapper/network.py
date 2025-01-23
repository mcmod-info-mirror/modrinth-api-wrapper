import httpx
from typing import Optional, Union

from modrinth_api_wrapper.expections import (
    ResponseCodeException,
    TooManyRequestsException,
    InvalidRequestException,
)

TIMEOUT = 3
CLIENT: httpx.Client = httpx.Client()


def request(
    url: str,
    method: str = "GET",
    data: Optional[dict] = None,
    params: Optional[dict] = None,
    json: Optional[dict] = None,
    headers: Optional[dict] = None,
    timeout: Optional[Union[int, float]] = TIMEOUT,
    **kwargs,
) -> dict:
    """
    HTTPX 请求函数
    """
    # delete null query
    if params is not None:
        params = {k: v for k, v in params.items() if v is not None}

    if json is not None:
        res: httpx.Response = CLIENT.request(
            method, url, json=json, params=params, timeout=timeout, headers=headers, **kwargs
        )
    else:
        res: httpx.Response = CLIENT.request(
            method, url, data=data, params=params, timeout=timeout, headers=headers, **kwargs
        )
    if res.status_code != 200:
        if res.status_code == 429:
            raise TooManyRequestsException(
                method=method,
                url=url,
                data=data if data is None else json,
                params=params,
            )
        elif res.status_code == 400:
            try:
                error = res.json()["error"]
                description = res.json()["description"]
            except:
                error = "Unknown"
                description = "Unknown"
            raise InvalidRequestException(
                method=method,
                url=url,
                data=data if data is None else json,
                params=params,
                error=error,
                description=description,
            )
        else:
            raise ResponseCodeException(
                status_code=res.status_code,
                method=method,
                url=url,
                data=data if data is None else json,
                params=params,
                msg=res.text,
            )
    return res.json()
