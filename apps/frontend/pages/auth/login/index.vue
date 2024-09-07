<script setup lang="ts">
    import { z } from "zod";
    import { toTypedSchema } from "@vee-validate/zod";

    const schema = z.object({
        username: z
            .string()
            .min(1, { message: "Username is required" })
            .max(50),
    });

    const validationSchema = toTypedSchema(schema);

    const { handleSubmit } = useForm({
        validationSchema,
        initialValues: {
            username: "",
        },
    });

    const onSubmit = handleSubmit((values) => {
        console.log(values);
    });
</script>

<template>
    <section class="w-full bg-background py-12">
        <div class="container px-4 md:py-6">
            <form @submit="onSubmit" class="space-y-6">
                <FormField v-slot="{ componentField }" name="username">
                    <FormItem>
                        <FormLabel>Username</FormLabel>
                        <FormControl>
                            <Input type="text" v-bind="componentField" />
                        </FormControl>
                        <FormDescription>
                            This is your public display name.
                        </FormDescription>
                        <FormMessage />
                    </FormItem>
                </FormField>
                <Button type="submit"> Submit </Button>
            </form>
        </div>
    </section>
</template>
