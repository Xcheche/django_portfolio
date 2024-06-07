from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    projects_show = [
        {
            "title": "Ecommerce",
            "path": "images/projects_img/ecom.jpeg",
        },
        {
            "title": "Salon",
            "path": "images/projects_img/hairsalon.jpeg",
        },
        {
            "title": "Portfolio",
            "path": "images/projects_img/portfolio_project.jpeg",
        },
    ]
    return render(request, "projects.html", {"projects_show": projects_show})


def experience(request):
    experience = [
        {
            "Company": "Google",
            "Position": "Software Engineer",
            "Duration": "2020-present",
        },
        {
            "Company": "Microsoft",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Arco",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Facebook",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Facebook",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Facebook",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
    ]
    return render(request, "experience.html", {"experience": experience})


def certificates(request):
    return render(request, "certificates.html")


def contact(request):
    return render(request, "contact.html")
