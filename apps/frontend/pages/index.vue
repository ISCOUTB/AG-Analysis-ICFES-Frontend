<script setup lang="ts">
    const { data, signIn } = useAuth();
</script>

<template>
    hello there
    <button @click="signIn('github')">Github</button>
    <pre>
        {{ data }}
    </pre>
</template>
