<script setup lang="ts">
    import {
        Select,
        SelectTrigger,
        SelectValue,
        SelectContent,
        SelectItem,
    } from "@/components/ui/select";

    const { data, signIn } = useAuth();
    const colorMode = useColorMode();

    const { characters } = await GqlCharacters();
</script>

<template>
    hello there
    <button @click="signIn('github')">Github</button>
    <pre>
        {{ data }}
    </pre>
    <Select
        :modelValue="$colorMode.preference"
        :onUpdate:modelValue="(value) => (colorMode.preference = value)"
    >
        <SelectTrigger>
            <SelectValue placeholder="Color mode" />
        </SelectTrigger>
        <SelectContent>
            <SelectItem value="system">System</SelectItem>
            <SelectItem value="light">Light</SelectItem>
            <SelectItem value="dark">Dark</SelectItem>
            <SelectItem value="sepia">Sepia</SelectItem>
        </SelectContent>
    </Select>
    <pre>
        {{ characters }}
    </pre>
</template>
