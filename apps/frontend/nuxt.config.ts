export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  modules: [
    // "nuxt-graphql-client",
    "@prisma/nuxt",
    "@sidebase/nuxt-auth",
  ],
  prisma: {
    autoSetupPrisma: true,
  },
  runtimeConfig: {
    AUTH_ORIGIN: process.env.AUTH_ORIGIN,
    AUTH_SECRET: process.env.AUTH_SECRET,
  },
  auth: {
    provider: {
      type: "authjs",
    },
    baseURL: process.env.AUTH_ORIGIN,
  },
});
