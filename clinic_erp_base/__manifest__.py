{
    "name": "Clinic ERP Base",
    "summary": "Core clinic patients, staff, rooms, and services",
    "version": "18.0.1.0.0",
    "category": "Healthcare",
    "license": "LGPL-3",
    "depends": ["base", "mail", "product"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/staff_views.xml",
        "views/room_views.xml",
        "views/service_views.xml",
        "views/menus.xml",
    ],
    "application": True,
    "installable": True,
}
