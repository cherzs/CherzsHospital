{
    "name": "Cherz Hospital",
    "version": "1.0",
    "sequence": -100,
    "summary": "Cherz Hospital",
    "description": "Cherz Hospital",
    "author": "Cherz Hospital",
    "category": "Hospital",
    "depends": ["base", "mail"],
    "data": [
        "security/hospital_security.xml",
        "data/sequence.xml",
        "views/patient_view.xml",
        "views/doctor_view.xml",
        "views/appointment_view.xml",
        "views/menu.xml",
    ],
    "demo": [
        "demo/doctor_demo.xml",
        "demo/patient_demo.xml",
        "demo/appointment_demo.xml",
    ],
    "auto_install": False,
    "application": True,
    "license": "LGPL-3",
    "images": ["static/description/icon.png"]
}
