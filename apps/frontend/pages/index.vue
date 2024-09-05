<script setup lang="ts">
    import { useAnalysisOptions } from "@/stores/analysisOptions";

    const analysisOptionsStore = useAnalysisOptions();
</script>

<template>
    <pre>{{ analysisOptionsStore }}</pre>
</template>
