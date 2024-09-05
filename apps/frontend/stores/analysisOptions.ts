enum ReportType {
    SABER11 = "SABER11",
    SABERPRO = "SABERPRO",
}

interface State {
    department: string | null;
    municipality: string | null;
    institution: string | null;
    reportType: ReportType;
}

export const useAnalysisOptions = defineStore("analysis-options", {
    state: (): State => ({
        department: null,
        institution: null,
        municipality: null,
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
            this.department = null;
            this.municipality = null;
            this.institution = null;
            this.reportType = ReportType.SABER11;
        },
    },
});
