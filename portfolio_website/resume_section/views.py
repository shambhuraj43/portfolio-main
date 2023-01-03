from django.shortcuts import render

# Create your views here.


def resume_page(request):
    context = {
        "projects": [
            {
                "name": "base",
                "technologies": "STRING OF TECHNOLOGIES"
            },
            {
                "name": "PROJECT1",
                "technologies": "STRING OF TECHNOLOGIES"
            },
            {
                "name": "PROJECT1",
                "technologies": "STRING OF TECHNOLOGIES"
            },
            {
                "name": "PROJECT1",
                "technologies": "STRING OF TECHNOLOGIES"
            }
        ]
    }
    return render(request, "resume_section/base.html", context)
