/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class ClinicWorkspace extends Component {
    static template = "clinic_erp_workspace.ClinicWorkspace";

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.state = useState({
            page: "calendar",
            loading: true,
            patients: [],
            doctors: [],
            appointments: [],
            visits: [],
            services: [],
            selectedDate: new Date().toISOString().slice(0, 10),
        });
        onWillStart(async () => this.loadData());
    }

    async loadData() {
        this.state.loading = true;
        const [patients, doctors, appointments, visits, services] = await Promise.all([
            this.orm.searchRead("clinic.patient", [], ["name", "phone", "national_id", "gender"]),
            this.orm.searchRead("clinic.staff", [["active", "=", true]], ["name", "department", "specialty", "staff_type", "room_id"]),
            this.orm.searchRead("clinic.appointment", [], ["name", "appointment_date", "appointment_time", "patient_id", "doctor_id", "department", "room_id", "state"]),
            this.orm.searchRead("clinic.visit", [], ["name", "visit_date", "visit_time", "patient_id", "doctor_id", "department", "room_id", "state"]),
            this.orm.searchRead("clinic.service", [["active", "=", true]], ["name", "department", "service_type", "price", "taxable"]),
        ]);
        Object.assign(this.state, { patients, doctors, appointments, visits, services, loading: false });
    }

    setPage(page) {
        this.state.page = page;
    }

    async openModel(model, resId = false) {
        await this.action.doAction({ type: "ir.actions.act_window", res_model: model, res_id: resId || false, views: [[false, "form"]], target: "current" });
    }

    newAppointment() {
        return this.openModel("clinic.appointment");
    }

    openAppointment(id) {
        return this.openModel("clinic.appointment", id);
    }

    openVisit(id) {
        return this.openModel("clinic.visit", id);
    }

    todaysAppointments() {
        return this.state.appointments.filter((item) => item.appointment_date === this.state.selectedDate);
    }

    waitingVisits() {
        return this.state.visits.filter((visit) => ["waiting", "with_doctor"].includes(visit.state));
    }

    displayName(value) {
        return Array.isArray(value) ? value[1] : "";
    }

    statusLabel(value) {
        return ({ booked: "Booked", waiting: "Waiting", with_doctor: "With Doctor", completed: "Completed", cancelled: "Cancelled" })[value] || value || "";
    }
}

registry.category("actions").add("clinic_erp.workspace", ClinicWorkspace);
