<script setup lang="ts">
    useHead({
        title: "Home Page",
    });
</script>

<template>
    <section :key="$route.fullPath">
        <HomeAnalysisOptions />
        <HomeAditionalOptions />
    </section>
</template>
