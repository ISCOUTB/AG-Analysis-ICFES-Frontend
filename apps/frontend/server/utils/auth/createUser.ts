import { prisma } from "@/lib/prisma";
import { User } from "@prisma/client";

export default async function (
    { name }: { name: string },
    { provider, providerAccountId }: ProviderInfo,
): Promise<User> {
    return await prisma.user.create({
        data: {
            name,
            email: `${name}-${provider}-${providerAccountId}@example.com`,
        },
    });
}
