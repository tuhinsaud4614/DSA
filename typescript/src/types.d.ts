export type Primitive = null | undefined | string | number | bigint | boolean;
export type NotFunction<T> = T extends Function ? never : T;
