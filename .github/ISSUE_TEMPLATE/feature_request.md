---
name: Feature Request
about: Suggest an idea for the BOSC Community Library
title: '[FEAT] '
labels: enhancement
assignees: ''

---

## Is your feature request related to a problem? Please describe.
**A clear and concise description of what the problem is.**
Currently, the library resources and navigation are only available in English. This creates a barrier for public-sector workers in rural areas who are more proficient in local languages like Luganda or Swahili. I'm frustrated when I see high-quality open-source resources that cannot be utilized by the very communities they are intended for due to language gaps.

## Describe the solution you'd like
**A clear and concise description of what you want to happen.**
I would like to implement a localization (i18n) framework. This includes:
1. Creating a `locales/` directory.
2. Storing translation strings in JSON files (e.g., `lug.json`, `swa.json`).
3. Updating the UI/README to allow users to toggle between languages.

## Describe alternatives you've considered
**A clear and concise description of any alternative solutions or features you've considered.**
* **Alternative 1:** Using browser-based auto-translation (Google Translate). However, this often misses technical context and local nuances.
* **Alternative 2:** Creating entirely separate repositories for different languages. This was rejected because it makes maintaining the core code twice as hard.

## Additional context
**Add any other context or screenshots about the feature request here.**
This aligns with the Ministry of Education's goal of "Digital Inclusion for All." Providing localized access ensures that the BOSC Community Library is truly a public-sector asset.