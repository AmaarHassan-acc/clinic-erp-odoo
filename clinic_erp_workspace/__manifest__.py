{
    "name": "Clinic ERP Workspace",
    "summary": "OWL backend workspace for receptionists and doctors",
    "version": "18.0.1.0.0",
    "category": "Healthcare",
    "license": "LGPL-3",
    "depends": ["clinic_erp_base", "clinic_erp_schedule", "clinic_erp_clinical", "clinic_erp_billing", "web"],
    "data": ["views/workspace_menus.xml"],
    "assets": {
        "web.assets_backend": [
            "clinic_erp_workspace/static/src/scss/clinic_workspace.scss",
            "clinic_erp_workspace/static/src/js/clinic_workspace.js",
            "clinic_erp_workspace/static/src/xml/clinic_workspace.xml",
        ],
    },
    "installable": True,
}
