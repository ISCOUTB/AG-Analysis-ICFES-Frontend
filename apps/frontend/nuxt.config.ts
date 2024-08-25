// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: "2024-04-03",
    devtools: { enabled: true },
    modules: ["@prisma/nuxt", "@sidebase/nuxt-auth"],
    prisma: {
        autoSetupPrisma: true,
    },
    runtimeConfig: {
        authSecret: process.env.AUTH_SECRET,
        githubClientId: process.env.GITHUB_CLIENT_ID,
        githubClientSecret: process.env.GITHUB_CLIENT_SECRET,
    },
    auth: {
        baseURL: process.env.AUTH_ORIGIN,
    },
});
