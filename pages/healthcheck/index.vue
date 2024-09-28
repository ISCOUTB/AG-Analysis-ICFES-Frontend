<script setup lang="ts">
    import type { GqlOps } from "#gql";
    import { capitalize } from "vue";

    definePageMeta({
        layout: false,
    });

    useHead({
        title: "HealthCheck",
    });

    interface OperationStatus {
        active: boolean;
        responseTime: number;
        loading: boolean;
    }

    const operations: GqlOps[] = [
        "colleges",
        "departments",
        "highschools",
        "municipalities",
        "periods",
    ];

    const operationStatus = ref<Record<GqlOps, OperationStatus>>(
        Object.fromEntries(
            operations.map((operation) => [
                operation,
                { active: false, responseTime: 0, loading: true },
            ]),
        ) as Record<GqlOps, OperationStatus>,
    );

    function checkOperationStatus(operation: GqlOps) {
        const startTime = performance.now();

        useAsyncGql({ operation })
            .then(
                () =>
                    (operationStatus.value[operation] = {
                        active: true,
                        responseTime: 0,
                        loading: false,
                    }),
            )
            .finally(() => {
                const endTime = performance.now();
                operationStatus.value[operation] = {
                    ...operationStatus.value[operation],
                    responseTime: endTime - startTime,
                };
            });
    }

    onMounted(() => {
        operations.forEach((operation) => checkOperationStatus(operation));
    });
</script>

<template>
    <section :key="$route.fullPath" class="w-full bg-background py-12">
        <div class="container px-4 md:px-6 flex flex-col gap-8">
            <template v-for="operation in operations" :key="operation">
                <div class="space-x-4 flex items-center">
                    <span class="font-bold text-2xl">{{
                        capitalize(operation)
                    }}</span>

                    <span class="w-full mx-4 h-[.075rem] bg-gray-300/50" />

                    <div class="flex items-center gap-4">
                        <div class="space-x-1">
                            <span class="font-bold">
                                {{
                                    operationStatus[
                                        operation
                                    ].responseTime.toFixed(2)
                                }}
                            </span>
                            <span class="italic text-sm">ms</span>
                        </div>

                        <span
                            v-if="operationStatus[operation].loading"
                            class="text-yellow-500 font-bold px-4 py-2 border border-yellow-500 rounded-md cursor-default"
                        >
                            Loading
                        </span>

                        <span
                            v-else-if="operationStatus[operation].active"
                            class="text-green-500 font-bold px-4 py-2 border border-green-500 rounded-md cursor-default"
                        >
                            Active
                        </span>
                        <span
                            v-else
                            class="text-rose-500 font-bold px-4 py-2 border border-rose-500 rounded-md cursor-default"
                        >
                            Not Active
                        </span>
                    </div>
                </div>
            </template>
        </div>
    </section>
</template>
