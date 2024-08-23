import { H3Error, H3Event } from "h3";
import { prisma } from "@/lib/prisma";
import { User } from "@prisma/client";

export default defineEventHandler(async (event: H3Event) => {
  try {
    const { email, password }: User = await readBody(event);

    const existingUser = await prisma.user.findUnique({
      where: { email },
    });

    if (existingUser)
      throw createError({
        statusCode: 400,
        statusMessage: "[ ERROR ] [ AUTH ] Email is already in use",
      });

    return await prisma.user.create({ data: { email, password } });
  } catch (error) {
    if (error instanceof H3Error) throw createError({ ...error, fatal: true });

    throw createError({
      status: 500,
      statusMessage: "[ FAILURE ] An unknown error ocurred",
    });
  }
});
