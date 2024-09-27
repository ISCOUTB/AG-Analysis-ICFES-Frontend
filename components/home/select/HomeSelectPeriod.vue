<script setup lang="ts">
    import { ReportType, useAnalysisOptions } from "@/stores/analysisOptions";

    const analysisStore = useAnalysisOptions();

    const reportType = computed(() => analysisStore.reportType);

    const { data } = useAsyncGql({
        operation: "periods",
        variables: {
            type: getType(),
        },
        options: {
            watch: [reportType],
        },
    });

    const filteredPeriods = computed(() => {
        if (!data.value) return [];

        return data.value.periods?.filter((period) => period !== null);
    });

    function getType(): string {
        switch (reportType.value) {
            case ReportType.SABER11:
                return "Saber11";

            case ReportType.SABERPRO:
                return "SaberPro";
        }
    }
</script>

<template>
    <div key="HomeSelectPeriod">
        <span class="font-semibold">Period</span>
        <Select
            :model-value="analysisStore.period"
            @update:model-value="(payload) => analysisStore.setPeriod(payload)"
        >
            <SelectTrigger class="mt-2">
                <SelectValue placeholder="Select a period" />
            </SelectTrigger>
            <SelectContent>
                <SelectItem
                    v-for="item in filteredPeriods"
                    :key="item.id"
                    :value="item.id"
                >
                    {{ item.label }}
                </SelectItem>
            </SelectContent>
        </Select>
    </div>
</template>
