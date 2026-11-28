const SEPARATORS = /[^a-z0-9]+/g;

export function slugify(title) {
  return title
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(SEPARATORS, "-")
    .replace(/^-+|-+$/g, "");
}
