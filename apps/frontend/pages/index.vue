<script setup lang="ts">
    const { session, loggedIn, fetch } = useUserSession();

    function handleSubmit(event: Event) {
        if (!(event.target instanceof HTMLFormElement)) return;

        const { elements } = event.target;
        const emailElement = elements.namedItem("email");
        const passwordElement = elements.namedItem("password");

        if (!(emailElement instanceof HTMLInputElement)) return;

        if (!(passwordElement instanceof HTMLInputElement)) return;

        const email = emailElement.value;
        const password = passwordElement.value;

        $fetch("/api/auth/login", {
            method: "POST",
            body: { email, password },
        })
            .then(() => {
                fetch();
            })
            .catch((error) => console.error(error));
    }

    const providers = [
        {
            label: "Github",
            to: "/api/auth/provider/github",
        },
    ];
</script>

<template>
    <AuthState #default="{ clear }">
        <form @submit.prevent="handleSubmit">
            <input type="text" name="email" class="border" />
            <input type="text" name="password" class="border" />
            <button>submit</button>
        </form>

        <button @click="clear">Sign out</button>

        <div>
            <NuxtLink
                v-for="provider in providers"
                :key="provider.label"
                :prefetch="false"
                :external="true"
                :to="provider.to"
            >
                Login with {{ provider.label }}
            </NuxtLink>
        </div>

        <pre>{{ session }}</pre>
        <pre>{{ loggedIn }}</pre>
    </AuthState>
</template>
