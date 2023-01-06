"""Config file to store necessary global varibles that are used through out the project.
"""

# Context for Independent Projects section on resume page.
projects_context = {
        "projects": [
            {
                "name": "Portfolio Website",
                "technologies": "Python, Django, Docker, GraphQL, GitHub Actions, AWS (Elastic Bean), Apache2, TDD, MySQL"
            },
            {
                "name": "REST API Project",
                "technologies": "Python, Django, Django - REST Framework, REST API, SQLite"
            },
            {
                "name": "Habit Tracker",
                "technologies": "MERN Stack, REST API, MongoDB NoSQL, Heroku, GitHub Pages, Docker"
            },
            {
                "name": "Software Design Calculator",
                "technologies":"Software Design, SOLID Principles"
            },
            {
                "name": "Random Contact Card",
                "technologies": "Node JS, Express, MongoDB, Third Party API Integration, Heroku"
            },
            {
                "name": "Weather Application",
                "technologies": "Node JS, Express, Third Party API Integration, Heroku"
            },
            {
                "name": "Path Finder",
                "technologies": "Java, Graph Theory"
            },
            {
                "name": "Banking Application",
                "technologies": "Java, OOP Concepts"
            }
        ]
    }

# Context to generate Project Pages.
project_page_context = {
        "portfolio": {
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