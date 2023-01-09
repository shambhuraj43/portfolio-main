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
        "web_page": False,
        "web_link": "Optimized_Software_Design_Calculator_App",
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
projects_information = {
    "portfolio-main": {
        "name": "Portfolio Website",
        "description": "I have built this website to provide information about myself. It contains my resume and the independent projects I have worked on as a Computer Science Undergraduate at IUPUI, Indianapolis.",
        "technolgies_used": [
            {
                "name": "Django - Python Framewrok",
                "description": "Built Django's MVT Architecture and ORM Feature",
                "icon": 'python',
                "icon_type": 'brands'
            },
            {
                "name": "Docker",
                "description": "Containerization with Docker Compose and Docker Hub Artifactory",
                "icon": "docker",
                "icon_type": "brands"
            },
            {
                "name": "MySQL & SQLite",
                "description": "Database for storing Project related Information",
                "icon": "database",
                "icon_type": "solid"
            },
            {
                "name": "GraphQL & REST API",
                "description": "CRUD Operations on Data with GraphQL (using Graphene), Django REST Framework",
                "icon": "circle-nodes",
                "icon_type": "solid",
            },
            {
                "name": "Git/GitHub",
                "description": "Source Code Management",
                "icon": "code-branch",
                "icon_type": "solid"
            },
            {
                "name": "GitHub Actions",
                "description": "CI/CD Pipeline, Automated linting, testing, building, containerization, pushing to Docker Hub Artifactory",
                "icon": "circle-play",
                "icon_type": "regular"
            },
            {
                "name": "Test Driven Development",
                "description": "Testing with PyTest Library",
                "icon": "screwdriver-wrench",
                "icon_type": "solid"
            },
            {
                "name": "Cloud Deployment",
                "description": "Python Anywhere Service, AWS",
                "icon": "cloud-arrow-up",
                "icon_type": "solid"
            },
            {
                "name": "Local Deployment",
                "description": "Apache2, Ubuntu",
                "icon": "server",
                "icon_type": "solid"
            },
        ],
        "installation_requirements": [
            {
                "req": "Django",
                "version": "4.1.4"
            },
            {
                "req": "Python",
                "version": "3.10"
            },
            {
                "req": "graphene-django",
                "version": "3.0.0"
            },
        ],
        "requirements_file": "Requirements.txt",
        "requirements_file_link": "https://github.com/shambhuraj43/portfolio-main/blob/main/requirements.txt",
        "github_repo_link": "https://github.com/shambhuraj43/portfolio-main"
    },
    "rest-api-django": {
        "name": "PROJECT_NAME",
        "description": "PROJECT_DESCRIPTION",
        "technolgies_used": [
            {
                "name": "Django - Python Framewrok",
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
