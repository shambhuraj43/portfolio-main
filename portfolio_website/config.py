"""Config file to store necessary global varibles that are used through out the project.
"""

# Context for Independent Projects section on resume page.
projects_context = {
    "portfolio-main": {
        "name": "Portfolio Website",
        "technologies": "Python, Django, Docker, GraphQL, GitHub Actions, AWS (Elastic Bean), Apache2, TDD, MySQL",
        "web_page": True,
        "web_link": "portfolio-main",
    },
    "rest-api-django": {
        "name": "REST API Project",
        "technologies": "Python, Django, Django - REST Framework, REST API, SQLite",
        "web_page": True,
        "web_link": "rest-api-django",
    },
    "Exercise-Tracker-App": {
        "name": "Habit Tracker",
        "technologies": "MERN Stack, REST API, MongoDB NoSQL, Heroku, GitHub Pages, Docker",
        "web_page": True,
        "web_link": "Exercise-Tracker-App",
    },
    "Software_Design_Calculator_App": {
        "name": "Software Design Calculator",
        "technologies": "Software Design, SOLID Principles",
        "web_page": True,
        "web_link": "Software_Design_Calculator_App",
    },
    "Random-User-Generator-React": {
        "name": "Random Contact Card",
        "technologies": "Node JS, Express, MongoDB, Third Party API Integration, Heroku",
        "web_page": False,
        "web_link": "Random-User-Generator-React",
    },
    "NodeJS_Weather_App": {
        "name": "Weather Application",
        "technologies": "Node JS, Express, Third Party API Integration, Heroku",
        "web_page": False,
        "web_link": "NodeJS_Weather_App",
    },
    "Pathfinder-Application": {
        "name": "Path Finder",
        "technologies": "Java, Graph Theory",
        "web_page": False,
        "web_link": "Pathfinder-Application",
    },
    "Banking_Application_Java": {
        "name": "Banking Application",
        "technologies": "Java, OOP Concepts",
        "web_page": False,
        "web_link": "Banking_Application_Java",
    }
}

# Context to generate Project Pages.
project_page_context = {
    "portfolio-main": {
        "project_name": "PROJECT_NAME",
        "project_description": "PROJECT_DESCRIPTION",
        "technolgies_used": [
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon": 'docker'
            },
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon": "none"
            },
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon": "none"
            },
        ],
        "installation_requirements": [
            {
                "req": "PYTHON",
                "version": "VERSION"
            },
            {
                "req": "PYTHON",
                "version": "VERSION"
            },
            {
                "req": "PYTHON",
                "version": "VERSION"
            },
        ],
        "requirements_file": "Requirements.txt",
        "requirements_file_link": "https://github.com/shambhuraj43/portfolio-main",
        "github_repo_link": "https://github.com/shambhuraj43/portfolio-main"
    },
    "django-rest-api": {
        "project_name": "PROJECT_NAME",
        "project_description": "PROJECT_DESCRIPTION",
        "technolgies_used": [
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon": 'docker'
            },
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon": "none"
            },
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon": "none"
            },
        ],
        "installation_requirements": [
            {
                "req": "PYTHON",
                "version": "VERSION"
            },
            {
                "req": "PYTHON",
                "version": "VERSION"
            },
            {
                "req": "PYTHON",
                "version": "VERSION"
            },
        ],
        "requirements_file": "Requirements.txt",
        "requirements_file_link": "https://github.com/shambhuraj43/portfolio-main",
        "github_repo_link": "https://github.com/shambhuraj43/portfolio-main"
    }
}
