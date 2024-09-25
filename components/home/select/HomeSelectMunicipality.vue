<script setup lang="ts">
    import { useAnalysisOptions } from "@/stores/analysisOptions";

    const analysisStore = useAnalysisOptions();

    const { filteredMunicipalities } = useHomeMunicipalities();
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
        {{ filteredMunicipalities }}
    </div>
</template>
