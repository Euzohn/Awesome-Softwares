# Add Software Workflow

This document outlines the process for adding new software to the Awesome Softwares repository. The project uses a structured data approach where all software information is stored in `data/software.json` and README files are auto-generated via `scripts/generate_readme.py`.

## Project Context

- **Data Source**: `data/software.json` (single source of truth for software data)
- **Generation Script**: `scripts/generate_readme.py` (generates `README.md` and `README.zh.md`)
- **Additional Scripts**: `scripts/add_software.py` (helper for adding software), `scripts/update_stars.py` (updates GitHub stars)
- **Categories**: See PROJECT_INFO.md for available software categories and their icons
- **Tags**: Use platform tags (#macOS, #Windows, #Linux, #Android, #iOS) and type tags (#开源软件, #免费软件, #付费软件, #跨平台)

## Workflow Steps

1. **User Input**: Provide the software's GitHub repository URL, official website URL, and logo link (optional). If logo not provided, prioritize finding the logo from the GitHub repository (e.g., in `icons/` or `assets/` directories). If not found there, search the official website or other sources. Once found, download and save the logo to the `images/` directory following the naming convention `{software-name}-logo.png`.

2. **Information Retrieval**: Use web search and web fetch tools to gather comprehensive software details including:
   - Software name
   - Description (English: `description_en`, Chinese: `description`)
   - Supported platforms (list from: macOS, Windows, Linux, Android, iOS, Web)
   - Open source status (`open_source`: boolean)
   - GitHub repository details (if applicable)
   - Cost model (`cost`: "free", "freemium", "paid"; `price`: optional price string, e.g., "$9.99" or "Freemium")
   - Key features/highlights (English: `highlights_en`, Chinese: `highlights`)
   - Tags (English: `tags_en`, Chinese: `tags`)
    - Category assignment (`category`: must select from the existing categories in `data/software.json` under the "categories" array. Check PROJECT_INFO.md for available categories and their descriptions.)
   - Logo path (`logo`: relative path in `images/`)

3. **Data Update**: Add the collected information to `data/software.json` following the existing JSON structure. Ensure proper categorization and all required fields are populated. **Important: Only add new entries; do not modify or delete existing software entries to avoid data loss.**

4. **Generate READMEs**: Execute `python scripts/generate_readme.py` to automatically regenerate `README.md` and `README.zh.md` from the updated data.

5. **Verification**: 
   - Check that the new software appears correctly in both README files under the appropriate category
   - Verify table of contents includes the new software
   - Test links and badges function properly
   - Run `python scripts/generate_readme.py` again if any issues are found

## Alternative Methods

- **Direct JSON Edit**: Manually edit `data/software.json` and run the generation script
- **Use Helper Script**: Run `python scripts/add_software.py --template` for a software entry template

## Notes

- Ensure all fields are populated in both English and Chinese where applicable
- Use consistent formatting matching existing entries
- Follow naming conventions for anchors and file paths
- **Critical: When adding software, only append new entries to the software list. Never modify or remove existing software entries to prevent accidental data loss.**
- Update GitHub stars periodically using `scripts/update_stars.py`
- Commit changes and push to trigger GitHub Actions for automated README updates