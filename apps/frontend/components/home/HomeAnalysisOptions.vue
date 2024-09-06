<script setup lang="ts">
    import { useAnalysisOptions, ReportType } from "@/stores/analysisOptions";

    const analysisStore = useAnalysisOptions();

    function handleReportTypeChange(payload: string | number) {
        const value = payload.toString();

        if (value !== ReportType.SABER11 && value !== ReportType.SABERPRO)
            return;

        analysisStore.setReportType(value);
    }
</script>

<template>
    <section class="w-full bg-background py-12">
        <div class="container px-4 md:px-6 grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-8">
                <div class="flex flex-col gap-4">
                    <span class="text-3xl font-bold">Advanced Analysis</span>
                    <span class="text-gray-600 dark:text-slate-50/70"
                        >Personalize your analysis options to obtain more
                        meaninful insights.</span
                    >
                </div>
                <div>
                    <span class="font-semibold">Report Type</span>
                    <Select @update:modelValue="handleReportTypeChange">
                        <SelectTrigger class="mt-2">
                            <SelectValue placeholder="Select the Report Type" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem
                                v-for="type in ReportType"
                                :value="type"
                            >
                                {{ type }}
                            </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </div>
            <div class="flex flex-col gap-4" (>
                <div>
                    <span class="font-semibold">Department</span>
                    <Select
                        :modelValue="analysisStore.department"
                        @update:modelValue="
                            (payload) => analysisStore.setDepartment(payload)
                        "
                    >
                        <SelectTrigger class="mt-2">
                            <SelectValue placeholder="Select a Department" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem value="value"> Buenos dias </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div>
                    <span class="font-semibold">Municipality</span>
                    <Select
                        :modelValue="analysisStore.municipality"
                        @update:modelValue="
                            (payload) => analysisStore.setMunicipality(payload)
                        "
                    >
                        <SelectTrigger class="mt-2">
                            <SelectValue placeholder="Select a Municipality" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem value="value"> Buenos dias </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
                <div>
                    <span class="font-semibold">Institution</span>
                    <Select
                        :modelValue="analysisStore.institution"
                        @update:modelValue="
                            (payload) => analysisStore.setInstitution(payload)
                        "
                    >
                        <SelectTrigger class="mt-2">
                            <SelectValue placeholder="Select a Institution" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem value="value"> Buenos dias </SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </div>
        </div>
    </section>
</template>
