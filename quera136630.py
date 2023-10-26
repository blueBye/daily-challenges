def sort_dependencies(packages, package_name):
    package_dependencies = []

    if len(packages[package_name]) == 0:
        return []
    
    for p in packages[package_name]:
        package_dependencies.extend(sort_dependencies(packages, p))
        package_dependencies.append(p)

    result = []
    [result.append(p) for p in package_dependencies if p not in result] 
    return result