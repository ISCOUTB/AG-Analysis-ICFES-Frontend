export default defineNuxtConfig({
    compatibilityDate: "2024-04-03",
    devtools: { enabled: true },
    modules: [
        "@prisma/nuxt",
        "@nuxtjs/tailwindcss",
        "shadcn-nuxt",
        "@nuxtjs/color-mode",
        "nuxt-graphql-client",
        "nuxt-auth-utils",
    ],
    prisma: {
        autoSetupPrisma: true,
    },
    shadcn: {
        prefix: "",
        componentDir: "./components/ui",
    },
    colorMode: {
        classSuffix: "",
    },
    experimental: {
        typedPages: true,
    },
});
