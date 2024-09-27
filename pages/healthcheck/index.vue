<script setup lang="ts">
    definePageMeta({
        layout: false,
    });

    const { data: departments } = useAsyncGql({
        operation: "departments",
    });
</script>

<template>
    <section :key="$route.fullPath" class="w-full bg-background py-12">
        <div class="container px-4 md:px-6 flex flex-col gap-4">
            <div class="space-x-4">
                <span class="font-bold text-2xl">Departments</span>
                <span
                    v-if="departments"
                    class="text-green-500 font-bold px-4 py-2 border border-green-500 rounded-md"
                >
                    Active
                </span>
                <span
                    v-else
                    class="text-rose-500 font-bold px-4 py-2 border border-green-500 rounded-md"
                >
                    Not Active
                </span>
            </div>
        </div>
    </section>
</template>
