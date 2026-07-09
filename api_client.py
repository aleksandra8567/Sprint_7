import requests
import logging

logger = logging.getLogger(__name__)

class ApiClient:
    @staticmethod
    def _request(method, url, **kwargs):
        logger.debug("%s %s, kwargs=%s", method, url, kwargs)
        response = requests.request(method, url, **kwargs)
        logger.debug("Response status=%s, body=%s", response.status_code, response.text)
        return response

    @classmethod
    def create_courier(cls, url, payload, timeout=5):
        return cls._request("POST", url, json=payload, timeout=timeout)

    @classmethod
    def courier_login(cls, url, payload, timeout=5):
        return cls._request("POST", url, json=payload, timeout=timeout)

    @classmethod
    def delete_courier(cls, url_template, courier_id, timeout=5):
        url = url_template.replace("{id}", str(courier_id))
        return cls._request("DELETE", url, timeout=timeout)

    @classmethod
    def create_order(cls, url, payload, timeout=5):
        return cls._request("POST", url, json=payload, timeout=timeout)

    @classmethod
    def get_orders_list(cls, url, params=None, timeout=5):
        return cls._request("GET", url, params=params, timeout=timeout)
