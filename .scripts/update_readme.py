import re
import yaml
from collections import defaultdict
from pathlib import Path

MONTH_ORDER = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']


def slugify(text):
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def parse_frontmatter(content):
    if not content.startswith('---'):
        return {}
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return {}


def get_all_tils(posts_dir):
    posts = []
    for md_file in Path(posts_dir).glob('*.md'):
        frontmatter = parse_frontmatter(md_file.read_text(encoding='utf-8'))
        if frontmatter and not frontmatter.get('draft', False):
            title = frontmatter.get('title')
            posts.append({
                'title': title,
                'date': frontmatter.get('created'),
                'url': f"https://huam.ing/{slugify(title)}",
                'tags': frontmatter.get('tags', []),
            })
    return sorted(posts, key=lambda post: post['date'], reverse=True)


def render_post(post):
    return f"* [{post['title']}]({post['url']})"


def render_details(label, body):
    parts = ["<details>", f"<summary>{label}</summary>", ""]
    if body:
        parts += [body, ""]
    parts.append("</details>")
    return "\n".join(parts)


def render_details_tree(tree, label):
    """Render nested <details> blocks; leaves are lists of posts, nodes are dicts."""
    blocks = []
    for key, value in tree.items():
        if isinstance(value, list):
            body = "\n".join(render_post(post) for post in value)
            blocks.append(render_details(f"{key} ({len(value)})", body))
        else:
            blocks.append(render_details_tree(value, key))
    return render_details(label, "\n\n".join(blocks))


def generate_recent_posts_section(posts, limit=5):
    return "\n".join(
        f"* **{post['date'].strftime('%Y-%m-%d')}** [{post['title']}]({post['url']})"
        for post in posts[:limit]
    )


def group_posts_by_category(posts):
    categories = defaultdict(list)
    for post in posts:
        for tag in post['tags']:
            categories[tag].append(post)
    return {tag: categories[tag] for tag in sorted(categories)}


def group_posts_by_date(posts):
    date_groups = defaultdict(lambda: defaultdict(list))
    for post in posts:
        date_groups[post['date'].year][post['date'].strftime('%B')].append(post)
    return {
        year: {
            month: date_groups[year][month]
            for month in sorted(date_groups[year], key=MONTH_ORDER.index, reverse=True)
        }
        for year in sorted(date_groups, reverse=True)
    }


def generate_toc(posts):
    word = "TIL" if len(posts) == 1 else "TILs"
    return "\n\n".join([
        f"[![Total {word}](https://img.shields.io/badge/Total%20{word}-{len(posts)}-blue?style=for-the-badge)](https://github.com/huaminghuangtw/Today-I-Learned/tree/main/posts)",
        "## Recent TILs",
        generate_recent_posts_section(posts),
        "## Browse All TILs",
        render_details_tree(group_posts_by_category(posts), "By Category"),
        render_details_tree(group_posts_by_date(posts), "By Date"),
    ])


def update_readme(readme_path, toc_content):
    start_marker = "<!-- index starts -->"
    end_marker = "<!-- index ends -->"

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    start_pos = readme_content.find(start_marker)
    end_pos = readme_content.find(end_marker)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(f"{readme_content[:start_pos + len(start_marker)]}\n{toc_content}\n{readme_content[end_pos:]}")


def main():
    root_dir = Path(__file__).parent.parent
    posts = get_all_tils(root_dir / 'posts')
    update_readme(root_dir / 'README.md', generate_toc(posts))


if __name__ == '__main__':
    main()
