import json
from requests import request as http_request
from devtodev_raw_export_wrapper.exceptions import DevtodevWrapperError, DevtodevApiError


class DevtodevWrapper:
    def __init__(self, user_api_token: str, **kwargs):
        self.__user_api_token = user_api_token
        self._api_endpoint = 'https://devtodev.com/api/v1/rawexport'
        self.app_id = kwargs.get('app_id', None)

    def _make_request(self, http_method: str, url: str, params: dict, headers: dict):
        """
        Общая функция отправки запросов к API.
        :param http_method: Метод запроса.
        :param url: Конечная точка запроса.
        :param params: Параметры запросы.
        :param headers: Заголовки запроса.
        :return:
        """
        params.update({'user_token': self.__user_api_token})

        try:
            response = http_request(http_method, url=url, data=json.dumps(params), headers=headers)

            if response.status_code in (200, 201):
                return response
            else:
                raise DevtodevApiError(response.json())
        except ConnectionError:
            raise DevtodevWrapperError(ConnectionError)

    def set_job(self, start_date: int, end_date: int, events: list = None, app_id: str = None) -> str:
        current_app_id = app_id or self.app_id
        events_list = events or []

        url = '/'.join((self._api_endpoint, 'setjob'))
        params = {
            'app_id': current_app_id,
            'start_date': start_date,
            'end_date': end_date,
            'events': events_list
        }
        headers = {}

        response = self._make_request('POST', url=url, params=params, headers=headers)
        return response.json()['data']

    def get_job_progress(self, job_id: str):
        url = '/'.join((self._api_endpoint, 'getprogress'))
        params = {
            'job_id': job_id
        }
        headers = {}

        response = self._make_request('POST', url=url, params=params, headers=headers)
        return response.json()['data']
