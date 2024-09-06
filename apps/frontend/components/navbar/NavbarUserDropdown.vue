<script setup lang="ts"> 
    import { providers } from "@/lib/providers";
    import { capitalize } from "vue";

    interface DropdownMenuItem {
        label: string;
        icon?: string;
        action?: () => unknown;
        subItems?: DropdownMenuItem[];
    }

    const { clear } = useUserSession();

    const dropdownMenuItems: DropdownMenuItem[] = [
        {
            label: "Sign up",
            subItems: providers.map(({ label, redirectTo }) => {
                return {
                    label,
                    action: () =>
                        navigateTo({ path: redirectTo }, { external: true }),
                    icon: `mdi:${label}`,
                };
            }),
        },
        {
            label: "Sign out",
            action: () => clear(),
        },
    ];

    const createAvatarFallback = (username?: string) => {
        return username
            ?.split(" ")
            .map((word) => word[0])
            .join("");
    };
</script>

<template>
    <AuthState>
        <template #default="{ user }">
            <DropdownMenu>
                <DropdownMenuTrigger>
                    <Avatar size="sm">
                        <AvatarImage :src="user?.image || '/default.jpg'" />
                        <AvatarFallback>
                            {{ createAvatarFallback(user?.name) }}
                        </AvatarFallback>
                    </Avatar>
                </DropdownMenuTrigger>
                <DropdownMenuContent>
                    <template v-for="item in dropdownMenuItems">
                        <DropdownMenuItem
                            v-if="!item.subItems"
                            @click="item.action"
                        >
                            {{ capitalize(item.label) }}
                        </DropdownMenuItem>
                        <DropdownMenuSub v-else>
                            <DropdownMenuSubTrigger>
                                {{ capitalize(item.label) }}
                            </DropdownMenuSubTrigger>
                            <DropdownMenuPortal>
                                <DropdownMenuSubContent>
                                    <DropdownMenuItem
                                        v-for="subItem in item.subItems"
                                        @click="subItem.action"
                                    >
                                        <div class="flex items-center gap-2">
                                            <Icon
                                                v-if="subItem.icon"
                                                :name="subItem.icon"
                                                class="text-lg"
                                            />
                                            <span>{{
                                                capitalize(subItem.label)
                                            }}</span>
                                        </div>
                                    </DropdownMenuItem>
                                </DropdownMenuSubContent>
                            </DropdownMenuPortal>
                        </DropdownMenuSub>
                    </template>
                </DropdownMenuContent>
            </DropdownMenu>
        </template>
    </AuthState>
</template>
