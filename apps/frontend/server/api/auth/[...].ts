import { NuxtAuthHandler } from "#auth";
import CredentialsProvider from "next-auth/providers/credentials";
import { prisma } from "~/lib/prisma";

const { AUTH_SECRET } = useRuntimeConfig();

export default NuxtAuthHandler({
  secret: AUTH_SECRET,
  providers: [
    // @ts-expect-error
    CredentialsProvider.default({
      name: "Credentials",
      credentials: {
        email: { label: "email", type: "email" },
        password: { label: "password", type: "password" },
      },
      async authorize(credentials: Record<"email" | "password", string>) {
        const user = await prisma.user.findUnique({
          where: { email: credentials.email },
        });

        if (!user) return null;

        if (credentials.password !== user.password)
          throw createError({
            statusCode: 400,
            statusMessage: "Incorrect Password",
            fatal: true,
          });

        return {
          email: user.email,
        };
      },
    }),
  ],
});
