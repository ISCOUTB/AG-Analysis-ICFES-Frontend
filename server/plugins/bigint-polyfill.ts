export default defineNitroPlugin(() => {
    BigInt.prototype.toJSON = function (): string {
        return this.toString();
    };
});
