<script setup lang="ts">
    import { useAnalysisOptions } from "@/stores/analysisOptions";

    const analysisStore = useAnalysisOptions();

    const { data } = useAsyncGql({
        operation: "colleges",
        variables: computed(() => ({
            municipalityId: analysisStore.municipality,
        })),
    });

    const filteredInstitutions = computed(() => {
        if (!analysisStore.municipality) return;

        return data.value.colleges?.filter((college) => college !== null);
    });
</script>

<template>
    <div>
        <span class="font-semibold">Institution</span>
        <Select
            :model-value="analysisStore.institution"
            :disabled="
                !analysisStore.municipality || !filteredInstitutions?.length
            "
            @update:model-value="
                (payload: string) => analysisStore.setInstitution(payload)
            "
        >
            <SelectTrigger class="mt-2">
                <SelectValue placeholder="Select a Institution" />
            </SelectTrigger>
            <SelectContent>
                <SelectItem
                    v-for="item in filteredInstitutions"
                    :key="item.id"
                    :value="item.id"
                >
                    {{ item.name }}
                </SelectItem>
            </SelectContent>
        </Select>
    </div>
</template>
