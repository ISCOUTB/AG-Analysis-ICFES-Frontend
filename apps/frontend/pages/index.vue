<script setup lang="ts">
  const { signIn, signOut, status, data } = useAuth();
  const loggedIn = computed(() => status.value === "authenticated");

  function handleRegister(event: Event): void {
    if (!(event.target instanceof HTMLFormElement)) return;

    const { elements } = event.target;

    const emailElement = elements.namedItem("email");
    const passwordElement = elements.namedItem("password");

    if (!(emailElement instanceof HTMLInputElement)) return;
    if (!(passwordElement instanceof HTMLInputElement)) return;

    const email = emailElement.value;
    const password = passwordElement.value;

    $fetch("/api/auth/register", {
      method: "POST",
      body: { email, password },
    })
      .then((response) => console.log(response))
      .catch((error) => console.error(error));
  }

  async function handleLogin(event: Event): Promise<void> {
    if (!(event.target instanceof HTMLFormElement)) return;

    const { elements } = event.target;

    const emailElement = elements.namedItem("email");
    const passwordElement = elements.namedItem("password");

    if (!(emailElement instanceof HTMLInputElement)) return;
    if (!(passwordElement instanceof HTMLInputElement)) return;

    const email = emailElement.value;
    const password = passwordElement.value;

    await signIn("credentials", { email, password });
  }
</script>

<template>
  <form @submit.prevent="handleRegister">
    <h1>Register</h1>
    <input name="email" type="email" placeholder="email" />
    <input name="password" type="password" placeholder="password" />
    <button>submit</button>
  </form>

  <form @submit.prevent="handleLogin">
    <h1>Login</h1>
    <input name="email" type="email" placeholder="email" />
    <input name="password" type="password" placeholder="password" />
    <button>submit</button>
  </form>

  <button v-if="loggedIn" @click="signOut()">Signout</button>

	<pre>{{ data }}</pre>
</template>
