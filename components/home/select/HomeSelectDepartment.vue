<script setup lang="ts">
    import { useAnalysisOptions } from "@/stores/analysisOptions";

    const analysisStore = useAnalysisOptions();

    const { data } = await useAsyncGql({
        operation: "departments",
    });

    const filteredDepartments = computed(() =>
        data.value.departments?.filter((department) => department !== null),
    );
</script>

<template>
    <div key="HomeSelectDepartment">
        <span class="font-semibold">Department</span>
        <Select
            :model-value="analysisStore.department"
            @update:model-value="
                (payload) => analysisStore.setDepartment(payload)
            "
        >
            <SelectTrigger class="mt-2">
                <SelectValue placeholder="Select a department" />
            </SelectTrigger>
            <SelectContent>
                <SelectItem
                    v-for="department in filteredDepartments"
                    :key="department.id"
                    :value="department.id"
                >
                    {{ department.name }}
                </SelectItem>
            </SelectContent>
        </Select>
    </div>
</template>
