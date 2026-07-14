{
    "name": "Clinic ERP Schedule",
    "summary": "Appointments, visits, and queue workflow",
    "version": "18.0.1.0.0",
    "category": "Healthcare",
    "license": "LGPL-3",
    "depends": ["clinic_erp_base", "calendar"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "views/appointment_views.xml",
        "views/visit_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
}
