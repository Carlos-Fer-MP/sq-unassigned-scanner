import json

from api.sonarqube import SonarQube
from utils.objects import application_list_data_refinement, portfolio_dictionary_refinement

'''
@list
Extracts the existing portfolios from SonarQube by name & key
'''


def get_sq_portfolios(base_url, http_basic_auth, environment):
    query = "components/search?qualifiers=VW&ps=500"
    request = SonarQube().get_instance_components(base_url, http_basic_auth, environment, query).text
    paging = json.loads(request)['paging']
    print("-------------------------------")
    print("total portfolios in " + environment + " " + str(paging.get("total")) + " 📖")
    print("-------------------------------")
    return json.loads(request)['components']


'''
@list
Extracts the existing applications from SonarQube by name & key
'''


def get_sq_applications(base_url, http_basic_auth, environment):
    query = "components/search?qualifiers=APP&ps=500"
    request = SonarQube().get_instance_components(base_url, http_basic_auth, environment, query).text
    paging = json.loads(request)['paging']
    print("-------------------------------")
    print("total apps in " + environment + " " + str(paging.get("total")) + " 📚")
    print("-------------------------------")

    return json.loads(request)['components']


'''
@list
Extracts the existing projects from SonarQube by name & key
'''


def get_sq_projects(base_url, http_basic_auth, environment):
    projects = []
    paging = None
    for page_num in range(1, 5):
        query = f"components/search?qualifiers=TRK&ps=500&p={page_num}"
        request = SonarQube().get_instance_components(base_url, http_basic_auth, environment, query).text
        paging = json.loads(request)['paging']
        projects.extend(json.loads(request)['components'])
    print("-------------------------------")
    print("total projects in " + environment + " " + str(paging.get("total")) + " 📙")
    print("-------------------------------")
    return projects


'''
@list
Gets the extended data of the portfolios to generate a final list of portfolios with their assigned applications
'''


def extend_sq_portfolio_data(existing_portfolios, base_url, http_basic_auth, environment):
    print("---------------------------------------------------------")
    print("Matching SonarQube portfolios with their data...  🗂️")
    portfolio_data = []
    for app in existing_portfolios:
        request = SonarQube().get_portfolio_data(base_url, http_basic_auth, environment, app.get("key")).text
        app_data = json.loads(request)
        portfolio_data.append(app_data.values())
    print("Data Matched Successfully! ✓")
    print("---------------------------------------------------------")
    print("")
    return portfolio_dictionary_refinement(portfolio_data)


'''
@list
Gets the extended data of the applications to generate a final list of portfolios with their assigned projects
'''


def extend_sq_application_data(existing_apps, base_url, http_basic_auth, environment):
    print("---------------------------------------------------")
    print("Matching SonarQube apps with their data...  🗃️")
    assigned_projects = []
    for app in existing_apps:
        request = SonarQube().get_application(base_url, http_basic_auth, environment, app.get("name")).text
        app_data = json.loads(request)
        assigned_projects.append(app_data.values())
    print("Data Matched Successfully! ✓")
    print("---------------------------------------------------")
    print("")
    return application_list_data_refinement(assigned_projects)


'''
@void
Matches the assigned projects from the applications with the total amount from SonarQube by name
'''


def extract_matching_projects(project_lst, assigned_projects_lst):
    matched_projects = []
    assigned_project_names = {project["name"] for entry in assigned_projects_lst for values in entry.values() for
                              project in values}

    for item in project_lst:
        if item["name"] in assigned_project_names:
            matched_projects.append(item)
    print("-------------------------------")
    print(f"Projects assigned correctly in Sonarqube: {len(matched_projects)}  ✅")
    print("-------------------------------")


'''
@void
Extracts the unassigned projects from the applications with the total amount from SonarQube by name
'''


def extract_unmatched_projects(project_lst, assigned_projects_lst):
    unmatched_projects = []
    app_project_names = {project["name"] for entry in assigned_projects_lst for values in entry.values() for project in
                         values}

    for item in project_lst:
        if item["name"] not in app_project_names:
            unmatched_projects.append(item)
    print("-------------------------------")
    print(f"Projects unassigned in Sonarqube: {len(unmatched_projects)} 📦")
    print("-------------------------------")

    for item in unmatched_projects:
        print(str(item["name"]))


'''
@Void
Matches the assigned applications from the portfolios with the total amount from SonarQube by name
'''


def extract_matched_applications(portfolio_lst, application_lst):
    portfolio_dict = {item[1]: item[5] for item in portfolio_lst}

    matched_applications = [
        item for item in application_lst
        if any(item["name"] in value.get('name') for values in portfolio_dict.values() for value in values)
    ]
    print("-------------------------------")
    print(f"Applications assigned correctly in Sonarqube: {len(matched_applications)}  ✅")
    print("-------------------------------")


'''
@void
Extracts the unassigned applications from the portfolios with the total amount from SonarQube by name
'''


def extract_unmatched_applications(portfolio_lst, application_lst):
    portfolio_dict = {item[1]: item[5] for item in portfolio_lst}

    unmatched_applications = [
        item for item in application_lst
        if all(item["name"] not in value.get('name') for values in portfolio_dict.values() for value in values)
    ]
    print("-------------------------------")
    print(f"Applications unassigned in Sonarqube: {len(unmatched_applications)} 📦")
    print("-------------------------------")

    for item in unmatched_applications:
        print(str(item["name"]))
