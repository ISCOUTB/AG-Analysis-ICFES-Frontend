import { prisma } from "@/lib/prisma";
import { H3Event } from "h3";

async function handleOnSuccess(
    event: H3Event,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    { user }: { user: any },
    provider: string,
) {
    const providerAccountId: string = user.id.toString();

    const _userAccount = await getUserAccount({
        provider,
        providerAccountId,
    });

    if (!_userAccount) {
        const createdUser = await createUser(
            { name: user.login },
            { provider, providerAccountId },
        );

        await createUserAccount(
            { userId: createdUser.id },
            { provider, providerAccountId },
        );

        await setSession(event, {
            email: createdUser.email,
            id: createdUser.id,
            image: user.avatar_url,
            name: createdUser.name || user.name,
        });

        return sendRedirect(event, "/");
    }

    const _user = await prisma.user.findUnique({
        where: { id: _userAccount.userId },
    });

    if (!_user)
        throw createError({
            statusCode: 500,
            statusMessage: "User not exists",
        });

    await setSession(event, {
        email: _user.email,
        id: _user.id,
        image: user.avatar_url,
        name: _user.name || user.name,
    });

    return sendRedirect(event, "/");
}

const providerHandlers: Record<string, (event: H3Event) => Promise<void>> = {
    github: oauthGitHubEventHandler({
        onSuccess: async (event, { user }) => {
            await handleOnSuccess(event, { user }, "github");
        },
    }),
};

export default defineEventHandler(async (event: H3Event) => {
    const providerName = getRouterParam(event, "providerName");

    if (!providerName)
        throw createError({
            statusCode: 400,
            statusMessage: "No provider were specified",
        });

    const providerHandler = providerHandlers[providerName];

    if (!providerHandler)
        throw createError({
            statusCode: 400,
            statusMessage: "Given provider isn't suported",
        });

    await providerHandler(event);
});
