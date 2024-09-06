export enum ReportType {
    SABER11 = "SABER11",
    SABERPRO = "SABERPRO",
}

interface State {
    department: string;
    municipality: string;
    institution: string;
    reportType: ReportType;
}

export const useAnalysisOptions = defineStore("analysis-options-store", {
    state: (): State => ({
        department: "",
        institution: "",
        municipality: "",
        reportType: ReportType.SABER11,
    }),
    actions: {
        setDepartment(payload: string) {
            this.department = payload;
        },

        setMunicipality(payload: string) {
            if (!this.department) return;
            this.municipality = payload;
        },

        setInstitution(payload: string) {
            if (!this.department || !this.department) return;
            this.institution = payload;
        },

        setReportType(payload: ReportType) {
            this.reportType = payload;
        },

        clear() {
            this.department = "";
            this.municipality = "";
            this.institution = "";
            this.reportType = ReportType.SABER11;
        },
    },
});
