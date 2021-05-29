declare module "str-utils" {
  type strUtil = (input: string) => string;
  export const strReverse: strUtil;
  export const strToLower: strUtil;
  export const strToUpper: strUtil;
  export const strRandomize: strUtil;
  export const strInvertCase: strUtil;
}
