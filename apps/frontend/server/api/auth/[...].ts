import { NuxtAuthHandler } from "#auth";
import GithubProvider from "next-auth/providers/github";
import { prisma } from "@/lib/prisma";
import { PrismaAdapter } from "@next-auth/prisma-adapter";

const { authSecret, githubClientId, githubClientSecret } = useRuntimeConfig();

export default NuxtAuthHandler({
    secret: authSecret,
    adapter: PrismaAdapter(prisma),
    providers: [
        // @ts-expect-error
        GithubProvider.default({
            clientId: githubClientId,
            clientSecret: githubClientSecret,
        }),
    ],
});
