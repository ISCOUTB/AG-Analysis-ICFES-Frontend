<script setup lang="ts">
    import {
        Avatar,
        AvatarFallback,
        AvatarImage,
    } from "@/components/ui/avatar";
    import { capitalize } from "vue";

    interface NavbarItem {
        label: string;
        to: string;
    }

    const items: NavbarItem[] = [
        {
            label: "features",
            to: "/",
        },
        {
            label: "pricing",
            to: "/",
        },
        {
            label: "about",
            to: "/",
        },
        {
            label: "contact",
            to: "/",
        },
    ];

    const createAvatarFallback = (username?: string) => {
        return username
            ?.split(" ")
            .map((word) => word[0])
            .join("");
    };
</script>

<template>
    <header class="w-full bg-background py-4 border-b">
        <div class="container px-4 md:px-6 flex items-center justify-between">
            <nav class="flex items-center gap-4 sm:gap-6">
                <NuxtLink v-for="item in items" :key="item.label" :to="item.to">
                    {{ capitalize(item.label) }}
                </NuxtLink>
            </nav>
            <AuthState>
                <template #default="{ user }">
                    <Avatar size="sm">
                        <AvatarImage :src="user?.image || '/default.jpg'" />
                        <AvatarFallback>
                            {{ createAvatarFallback(user?.name) }}
                        </AvatarFallback>
                    </Avatar>
                </template>
            </AuthState>
        </div>
    </header>
</template>
