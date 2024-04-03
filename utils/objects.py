"""
I am a
multi-line comment!
"""

'''
Reformat the given raw dictionaries of portfolios with multiple layers of unnecessary data
'''


def portfolio_dictionary_refinement(lst):
    raw_data_lst = []
    for elements in lst:
        tmp_dictionary = {index: value for index, value in enumerate(elements)}
        raw_data_lst.append(tmp_dictionary)
    return raw_data_lst


'''
Reformat the given raw application list with multiple layers of unnecessary data
'''


def application_list_data_refinement(lst):
    raw_data_lst = []
    for elements in lst:
        tmp_dictionary = {index: value for index, value in enumerate(elements)}
        raw_data_lst.append(tmp_dictionary)
    return projects_assigned_formatter(raw_data_lst)


'''
Reformat the given raw project dictionary with multiple layers of unnecessary data to maintain only required key name
'''


def project_data_refinement(dictionary):
    cleaned_list = [
        {key: value for key, value in elements.items() if key not in ["key", "qualifier", "project"]}
        for elements in dictionary if isinstance(elements, dict)
    ]
    return cleaned_list


'''
Generate a new dictionary for projects with the keys "name" as a new key with the value of "projects"
'''


def projects_assigned_formatter(application_lst):
    formatted_list = [
        {values.get("name"): values.get("projects")}
        for elements in application_lst
        for keys, values in elements.items()
        if isinstance(values, dict)
    ]
    return formatted_list
