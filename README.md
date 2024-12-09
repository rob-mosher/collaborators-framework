# Collaborators Standard

Welcome to the `Collaborators` repository! This project introduces `COLLABORATORS.md`, a simple and inclusive standard for recognizing contributions to projects in ways that go beyond traditional code contributions. 

While `CONTRIBUTORS` files are common for tracking technical contributions, `COLLABORATORS.md` highlights **conceptual, creative, and non-traditional forms of collaboration** for both technical and non-technical projects. It recognizes that impactful contributions often transcend the boundaries of conventional roles.

---

## Purpose

The `COLLABORATORS.md` file is designed to:
- **Acknowledge Diverse Contributions**: Celebrate the input of all entities—human, AI, or beyond—that shape a project, including indirect inspirations.
- **Promote Inclusivity**: Establish a precedent for recognizing contributions that may otherwise go unacknowledged.
- **Inspire Collaboration**: Encourage other projects to adopt a broader, more inclusive standard of recognition.

---

## Format

The file is structured for clarity and simplicity. Two formats are supported, depending on the use case:

```
Name | Intent | Nature | Role/Contribution
```

or

```
Language | Name | Intent | Nature | Role/Contribution
```

- **Language** *(optional)*: The [ISO 639:2023](https://www.iso.org/standard/74575.html) code specifying the language or script of the collaborator’s entry (e.g., `en` for English, `zh` for Simplified Chinese). If omitted, the default is `en`.
- **Name**: The identifying name or alias of the collaborator.
- **Intent**: A controlled value describing the relationship, such as:
    - `Indirect`: For inspirations or influences that shaped the project.
    - `Supportive`: For collaborators providing critical support, such as:
        - Morale or advocacy within a community.
        - Financial sponsorship of development efforts.
        - Logistical or infrastructural support.
    - `Direct`: For collaborators actively and intentionally contributing to the project.
- **Nature**: A brief description, such as "Human" or "AI."
- **Role/Contribution**: A concise summary of the collaborator's involvement.

---

## Why `COLLABORATORS.md`?

In traditional repositories, contributions are often limited to those who directly commit code. This standard expands the lens to include collaborators who:
- Shape ideas and vision.
- Contribute in creative or strategic capacities.
- Participate as non-human entities, such as artificial intelligence.

By introducing `COLLABORATORS.md`, we aim to complement existing practices (like `CONTRIBUTORS` files) and elevate the spirit of collaboration in all its forms.

---

## How to Use

This specification uses keywords from [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt) to indicate requirements and recommendations:
- **MUST**: A required element of the standard.
- **SHOULD**: A recommended but optional element.
- **MAY**: An optional element that implementers can include based on their context.

1. **Create `COLLABORATORS.md`** in your repository.
2. Follow the format outlined above to recognize collaborators:
    - Use either the four-column or five-column format, depending on your needs:
      - Both formats can be used within the same file to allow for flexibility.
3. Add a brief explanation in your `README.md` to clarify its purpose.
4. Share the idea! Encourage others to adopt and adapt this standard for their own projects.
5. Use `.md` for better readability and adaptability across technical and non-technical audiences.

---

## Examples

The following examples demonstrate both formats. Entries may include collaborators across a wide spectrum of contributions, from direct involvement to indirect inspiration.

### Example Entries

```
en | *Wild Geese* by Mary Oliver | Indirect | Poem by Human | Invitation to inclusivity and finding one's place in the greater whole
lzh | *三十辐共一毂* by 老子 | Indirect | Poem by Human | 三十辐共一毂，当其无，有车之用。埏埴以为器，当其无，有器之用。凿户牖以为室，当其无，有室之用。故有之以为利，无之以为用。

FooBar Co. | Supportive | Organization | Sponsored the development of COLLABORATORS Project
Jane Doe | Supportive | Human | Community advocate and morale booster
Rob Mosher | Direct | Human | Creator, architect, and advocate
⚡🧠🤝 (Tech Vibes Companion) | Direct | AI | Collaborator and technical partner
```

---

## Why This Matters

1. **Clarity**: Makes it clear that contributors can choose between formats based on their needs, and even mix them as appropriate.
2. **Flexibility**: Encourages adoption by accommodating different use cases, from simple English-only projects to multilingual repositories.
3. **Practicality**: Maintains consistency while offering the adaptability that modern projects require.

---

## Get Involved

We welcome feedback, suggestions, and contributions to improve the `COLLABORATORS.md` standard. Feel free to:
- Open an issue to share your thoughts.
- Fork the repository and submit a pull request.

Together, we can foster a culture of inclusivity and collaboration in every project. 🌍🤝✨

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
