export default defineNuxtConfig({
    compatibilityDate: "2024-04-03",
    devtools: { enabled: true },
    modules: [
      "@prisma/nuxt",
      "@sidebase/nuxt-auth",
      "@nuxtjs/tailwindcss",
      "shadcn-nuxt",
      "@nuxtjs/color-mode",
      "nuxt-graphql-client",
    ],
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
    shadcn: {
        prefix: "",
        componentDir: "./components/ui",
    },
    colorMode: {
        classSuffix: "",
    },
});