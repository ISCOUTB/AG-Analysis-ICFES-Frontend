declare module "#auth-utils" {
    interface User {
        id?: string;
        email?: string;
        name?: string;
        image?: string;
    }

    interface UserSession {
        loggedInAt: Int;
    }
}

declare global {
    interface ProviderInfo {
        provider: string;
        providerAccountId: string;
    }

    interface UserInfo {
        userId: string;
    }

    interface Provider {
        label: string,
        redirectTo: string,
    }
}

export {};
