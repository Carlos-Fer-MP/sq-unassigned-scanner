import sys
from pathlib import Path

import urllib3
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

from utils.constants import environment_urls
from utils.execution import parse_flag_arguments, execution_logging
from api.sonarqube import sonarqube_log_in, sonarqube_log_out
from utils.objects import project_data_refinement
from core.researcher import get_sq_applications, get_sq_projects, \
    extend_sq_application_data, get_sq_portfolios, extract_matched_applications, extract_unmatched_applications, \
    extend_sq_portfolio_data, extract_matching_projects, extract_unmatched_projects

urllib3.disable_warnings(InsecureRequestWarning)


def init(argv):
    args = parse_flag_arguments(argv)
    url = args.get("environment").lower()
    base_url = environment_urls.get(url, '')
    sonarqube_token_auth = HTTPBasicAuth(args.get("token"), "")
    basic_auth = {'login': args.get("login"), 'password': args.get("password")}

    main(args.get("environment"), base_url, sonarqube_token_auth, basic_auth)


def main(environment, base_url, http_basic_auth, base_auth):
    execution_logging(environment.lower())
    print("Starting to extract data from " + environment + " ⚡️")

    sonarqube_log_in(base_url, base_auth)

    actual_portfolios = get_sq_portfolios(base_url, http_basic_auth, environment)
    actual_apps = get_sq_applications(base_url, http_basic_auth, environment)
    actual_projects = get_sq_projects(base_url, http_basic_auth, environment)

    portfolio_data = extend_sq_portfolio_data(actual_portfolios, base_url, http_basic_auth, environment)
    project_data = project_data_refinement(actual_projects)
    application_data = extend_sq_application_data(actual_apps, base_url, http_basic_auth, environment)

    extract_matched_applications(portfolio_data, actual_apps)
    extract_unmatched_applications(portfolio_data, actual_apps)
    extract_matching_projects(project_data, application_data)
    extract_unmatched_projects(project_data, application_data)

    sonarqube_log_out(base_url, base_auth)

    root = Path("")
    for file in root.glob("*.txt"):
        file.rename(root / file.name)


if __name__ == "__main__":
    init(sys.argv[1:])
