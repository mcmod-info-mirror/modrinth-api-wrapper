from typing import Optional

class ApiException(Exception):
    """
    API 异常基类。
    """

    def __init__(
        self,
        msg: str = "出现了错误，但是未说明具体原因。",
        method: str = "GET",
        url: Optional[str] = None,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        self.msg = msg
        self.method = method
        self.url = url
        self.params = params
        self.data = data

    def __str__(self):
        return (
            f"API Exception:\n"
            f"Message: {self.msg}\n"
            f"Method: {self.method}\n"
            f"URL: {self.url}\n"
            f"Params: {self.params}\n"
            f"Data: {self.data}"
        )

class ResponseCodeException(ApiException):
    """
    API 返回 code 错误。
    """

    def __init__(
        self,
        status_code: int,
        msg: str = "出现了错误，但是未说明具体原因。",
        url: Optional[str] = None,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        method: str = "GET",
    ):
        """
        Args:
            status_code (int): 错误代码。
        """
        super().__init__(msg, method, url, params, data)
        self.status_code = status_code

    def __str__(self):
        return (
            f"Response Code Exception:\n"
            f"Status Code: {self.status_code}\n"
            f"Message: {self.msg}\n"
            f"Method: {self.method}\n"
            f"URL: {self.url}\n"
            f"Params: {self.params}\n"
            f"Data: {self.data}"
        )

# 429 Too Many Requests
class TooManyRequestsException(ResponseCodeException):
    def __init__(self, url: str, params: dict, data: dict, method: str):
        super().__init__(
            status_code=429,
            msg="Too Many Requests",
            url=url,
            params=params,
            data=data,
            method=method,
        )

class TimeoutException(ApiException):
    def __init__(self, url: str, params: dict, data: dict, method: str):
        super().__init__(
            msg="Timeout", url=url, params=params, data=data, method=method
        )

class InvalidRequestException(ResponseCodeException):
    """
    400 Bad Request
    """
    def __init__(self, url: str, params: dict, data: dict, method: str, error: str, description: str):
        super().__init__(
            status_code=400,
            msg=f"Invalid Request: {error} {description}",
            url=url,
            params=params,
            data=data,
            method=method,
        )