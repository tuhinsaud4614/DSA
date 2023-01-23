export type Primitive = null | undefined | string | number | bigint | boolean;
export type NotFunction<T> = T extends Function ? never : T;
export type NodeObjectType<T> = { id: string; value: T; next?: NodeObjectType<T>, previous?: NodeObjectType<T>};
