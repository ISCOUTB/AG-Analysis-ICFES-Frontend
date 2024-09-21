<script setup lang="ts">
    import { useAnalysisOptions } from "@/stores/analysisOptions";

    const analysisStore = useAnalysisOptions();

    const { data } = await useAsyncGql({
        operation: "municipalities",
        variables: computed(() => ({
            departmentId: analysisStore.department,
        })),
    });

    const filteredMunicipalities = computed(() => {
        if (!analysisStore.department) return;
        return data.value.municipalities?.filter(
            (municipality) => municipality !== null,
        );
    });
</script>

<template>
    <div>
        <span class="font-semibold">Municipality</span>
        <Select
            :model-value="analysisStore.municipality"
            :disabled="
                !analysisStore.department || !filteredMunicipalities?.length
            "
            @update:model-value="
                (payload: string) => analysisStore.setMunicipality(payload)
            "
        >
            <SelectTrigger class="mt-2">
                <SelectValue placeholder="Select a Municipality" />
            </SelectTrigger>
            <SelectContent>
                <SelectItem
                    v-for="municipality in filteredMunicipalities"
                    :key="municipality.id"
                    :value="municipality.id"
                >
                    {{ municipality.name }}
                </SelectItem>
            </SelectContent>
        </Select>
    </div>
</template>
