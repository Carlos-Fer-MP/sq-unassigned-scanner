import requests

from utils.constants import ssl_certificate_route

constant_content_type = {'Content-Type': 'application/x-www-form-urlencoded'}


def sonarqube_log_in(base_url, base_auth):
    url = base_url + "authentication/login"
    headers = constant_content_type
    requests.post(url, headers=headers, data=base_auth, verify=ssl_certificate_route)


def sonarqube_log_out(base_url, base_auth):
    url = base_url + "authentication/logout"
    headers = constant_content_type
    requests.post(url, headers=headers, data=base_auth, verify=ssl_certificate_route)


class SonarQube:
    base_url = None
    requests = None
    http_basic_auth = None
    environment = None
    data = {}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def get_portfolio_data(self, base_url, basic_auth, environment, key):
        self.base_url = base_url
        self.requests = requests
        self.http_basic_auth = basic_auth
        self.environment = environment
        url = base_url + "views/show?key=" + key
        return requests.request(
            "GET",
            url,
            headers=self.headers,
            data=self.data,
            auth=self.http_basic_auth,
            verify=ssl_certificate_route
        )

    def get_application(self, base_url, basic_auth, environment, application):
        self.base_url = base_url
        self.requests = requests
        self.http_basic_auth = basic_auth
        self.environment = environment
        url = base_url + "applications/show?application=" + application

        return requests.request(
            "GET",
            url,
            headers=self.headers,
            data=self.data,
            auth=self.http_basic_auth,
            verify=ssl_certificate_route
        )

    def get_instance_components(self, base_url, basic_auth, environment, query):
        self.base_url = base_url
        self.requests = requests
        self.http_basic_auth = basic_auth
        self.environment = environment
        url = base_url + query

        return requests.request(
            "GET",
            url,
            headers=self.headers,
            data=self.data,
            auth=self.http_basic_auth,
            verify=ssl_certificate_route
        )
