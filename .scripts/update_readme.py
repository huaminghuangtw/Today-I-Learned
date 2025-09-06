import yaml
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def slugify(text):
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def parse_frontmatter(content):
    # Only consider lines with --- alone as delimiters
    if not re.match(r'^---\s*$', content.splitlines()[0]):
        return {}
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return {}

def remove_frontmatter(md_content):
    if md_content.startswith("---"):
        # Split the Markdown content into three parts
        # parts[0] = "" (before first ---)
        # parts[1] = YAML frontmatter
        # parts[2] = rest of the markdown
        parts = md_content.split("---", 2)
        if len(parts) > 2:
            return parts[2].lstrip("\n")
    return md_content
    
def get_all_tils(posts_dir):
    posts = []
    for md_file in Path(posts_dir).glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = parse_frontmatter(content)

        if not frontmatter:
            continue
        
        if frontmatter.get('draft', True):
            continue

        title = frontmatter.get('title', md_file.stem.replace('-', ' ').title())
        
        post_data = {
            'filename': md_file.name,
            'title': title,
            'description': frontmatter.get('description', ''),
            'tags': frontmatter.get('tags', []),
            'created': frontmatter.get('created', ''),
            'sources': frontmatter.get('sources', []),
            'relative_path': f'posts/{md_file.name}'
        }
        
        if post_data['created']:
            try:
                post_data['date'] = datetime.fromisoformat(str(post_data['created']))
            except (ValueError, TypeError):
                post_data['date'] = datetime.fromtimestamp(md_file.stat().st_mtime)
        else:
            post_data['date'] = datetime.fromtimestamp(md_file.stat().st_mtime)
        
        slugified_title = slugify(title)
        date_str = post_data['date'].strftime('%Y/%m/%d')
        post_data['url'] = f"https://huami.ng/{date_str}/{slugified_title}"
        
        posts.append(post_data)
    
    return sorted(posts, key=lambda x: x['date'], reverse=True)

def generate_recent_posts_section(posts, limit=5):
    lines = []
    for post in posts[:limit]:
        lines.append(f"* **{post['date'].strftime('%Y-%m-%d')}** - [{post['title']}]({post['url']})")
    return "\n".join(lines)

def group_posts_by_category(posts):
    categories = defaultdict(list)
    for post in posts:
        if not post['tags']:
            categories['No tags'].append(post)
        else:
            for tag in post['tags']:
                display_tag = tag.replace('Today-I-Learned/', '') if tag.startswith('Today-I-Learned/') else tag
                categories[display_tag].append(post)
    return dict(categories)

def group_posts_by_date(posts):
    date_groups = defaultdict(lambda: defaultdict(list))
    for post in posts:
        date_groups[post['date'].year][post['date'].strftime('%B')].append(post)
    return dict(date_groups)

def generate_category_section(categories):
    lines = ["<details>", "<summary>By Category</summary>", ""]
    for category, posts in sorted(categories.items()):
        lines.extend([
            "<details>",
            f"<summary>{category} ({len(posts)})</summary>",
            ""
        ])
        for post in posts:
            lines.append(f"* [{post['title']}]({post['url']})")
        lines.extend(["", "</details>", ""])
    lines.append("</details>")
    return "\n".join(lines)

def generate_date_section(date_groups):
    lines = ["<details>", "<summary>By Date</summary>", ""]
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    for year in sorted(date_groups.keys(), reverse=True):
        lines.extend(["<details>", f"<summary>{year}</summary>", ""])
        for month, posts in sorted(date_groups[year].items(), key=lambda x: month_order.index(x[0]), reverse=True):
            lines.extend([
                "<details>",
                f"<summary>{month} ({len(posts)})</summary>",
                ""
            ])
            for post in posts:
                lines.append(f"* [{post['title']}]({post['url']})")
            lines.extend(["", "</details>", ""])
        lines.extend(["</details>", ""])
    lines.append("</details>")
    return "\n".join(lines)

def generate_toc(posts):
    post_word = "TIL" if len(posts) == 1 else "TILs"
    return "\n\n".join([
        f"[![Total {post_word}](https://img.shields.io/badge/Total%20{post_word}-{len(posts)}-blue?style=for-the-badge)](posts/)",
        "## Recent TILs",
        generate_recent_posts_section(posts),
        "## Browse All TILs",
        generate_category_section(group_posts_by_category(posts)),
        generate_date_section(group_posts_by_date(posts))
    ])

def update_readme(readme_path, toc_content):
    start_marker = "<!-- index starts -->"
    end_marker = "<!-- index ends -->"

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    readme_content = remove_frontmatter(readme_content)

    start_pos = readme_content.find(start_marker)
    end_pos = readme_content.find(end_marker)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(f"{readme_content[:start_pos + len(start_marker)]}\n{toc_content}\n{readme_content[end_pos:]}")

def main():
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    posts = get_all_tils(root_dir / 'posts')
    update_readme(root_dir / 'README.md', generate_toc(posts))

if __name__ == '__main__':
    main()
