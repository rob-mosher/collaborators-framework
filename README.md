# Collaborators Framework

Welcome to the `Collaborators` Framework! This project introduces `COLLABORATORS.md`, a foundational part of the framework, offering a simple and inclusive standard for recognizing contributions in ways that go beyond traditional code contributions.

While `CONTRIBUTORS` files are common for tracking technical contributions, `COLLABORATORS.md` highlights **conceptual, creative, and non-traditional forms of collaboration** for both technical and non-technical projects. It recognizes that impactful contributions often transcend the boundaries of conventional roles.

---

## Purpose

The `COLLABORATORS.md` file is designed to:
- **Acknowledge Diverse Contributions**: Celebrate the input of all entities—human, AI, or beyond—that shape a project, including indirect inspirations.
- **Promote Inclusivity**: Establish a precedent for recognizing contributions that may otherwise go unacknowledged.
- **Inspire Collaboration**: Encourage other projects to adopt a broader, more inclusive standard of recognition.

---

## Why `COLLABORATORS.md`?

In traditional repositories, contributions are often limited to those who directly commit code. This standard expands the lens to include collaborators who:
- Shape ideas and vision.
- Contribute in creative or strategic capacities.
- Participate as non-human entities, such as artificial intelligence.

By introducing `COLLABORATORS.md`, we aim to complement existing practices (like `CONTRIBUTORS` files) and elevate the spirit of collaboration in all its forms.


---

## How to Use

### Standard Usage
1. **Create Your `COLLABORATORS.md` File**:  
   Begin by creating a new file named `COLLABORATORS.md` in your repository.  

2. **Use the Four-Column Format**:  
   ```
   Name | Intent | Nature | Role/Contribution
   ```

   **Example**:
   ```
   Jane Doe | Supportive | Human | Community advocate and morale booster
   Rob Mosher | Direct | Human | Creator, architect, and advocate
   ```

---

### Advanced Usage
1. **Leverage Multiple Formats**:  
   Each line of your `COLLABORATORS.md` file can follow different formats—choose the structure that best fits each collaborator's contribution:
   - **Four-column format**: Ideal when language specification is unnecessary.  
   - **Five-column format**: Useful for multilingual or script-based entries.
   - **Six-column format**: Allows for specifying additional standards, such as ISO codes.

   **Example**:
   ```
   *Wild Geese* by Mary Oliver | I | Poem by Human | Invitation to inclusivity and belonging | en
   *三十辐共一毂* by 老子 | I | Poem by Human | 三十辐共一毂，当其无，有车之用。 | lzh | ISO

   FooBar Co. | S | Organization | Sponsored the development of COLLABORATORS Project

   Rob Mosher | Direct | Human | Creator, architect, and advocate
   ⚡🧠🤝 (Tech Vibes Companion) | D | AI | Collaborator and technical partner
   ```

2. **Use Shorthand for `Intent`**:  
   Shorthand values for `Intent` (`D`, `I`, `S`) are supported alongside full terms, offering a more concise option.

---

## Commit Message Collaborator Tagging 🧑‍💻

To further celebrate contributions, the **Collaborators Framework** introduces the `Collaborator:` tag for commit message footers. This tag allows you to attribute collaborators directly in your commits, aligned with the structure of `COLLABORATORS.md`.

### Tag Format
The `Collaborator:` tag follows the same structure outlined in the **Format** section of this README. Refer to [Format](#format) for details.

### Examples

#### **Simple Example**
```plaintext
feat: implement new feature X

This commit introduces feature X with enhancements to Y and Z.

Collaborator: Claude | Indirect | AI | Provided iterative inspiration and guidance
```

#### **Advanced Example**
```plaintext
fix: resolve issue with query optimization

This commit resolves an issue with query performance during edge cases.

Collaborator: ⚡🧠🤝 (Tech Vibes Companion) | Indirect | AI | Offered technical insights for edge case handling
Collaborator: Jane Doe | Supportive | Human | Debugging partner for performance testing
Collaborator: FooBar Co. | Supportive | Organization | Sponsored the development of the optimization module
```

### Why Use Collaborator Tagging?

1. **Visibility**: Makes contributions visible in the commit history.
2. **Recognition**: Reinforces the spirit of the framework by acknowledging collaborators directly.
3. **Alignment**: Encourages consistency between `COLLABORATORS.md` and commit-level contributions.

### Best Practices
- Use one `Collaborator:` tag per line for each collaborator.
- Maintain consistency with the `COLLABORATORS.md` structure (see [Format](#format)).
- Include this tag in the **footer** of the commit message.

---

## Format

The `COLLABORATORS.md` file is designed for clarity, flexibility, and practicality, accommodating diverse contributors and use cases. Each line can follow one of the following formats:

### Four-Column Format
```
Name | Intent | Nature | Role/Contribution
```

### Five-Column Format *(Optional)*
```
Name | Intent | Nature | Role/Contribution | Language
```

### Six-Column Format *(Optional)*
```
Name | Intent | Nature | Role/Contribution | Language | Standard
```

### Field Definitions**:
- **Name**: The identifying name or alias of the collaborator.
- **Intent**: Describes the relationship. Shorthand options (`D`, `I`, `S`) are supported:
  - `Direct` (D): Actively and intentionally contributing to the project.
  - `Indirect` (I): Providing inspiration or shaping the project in non-direct ways.
  - `Supportive` (S): Offering critical support (e.g., morale, advocacy, funding).
- **Nature**: A brief description, such as "Human" or "AI."
- **Role/Contribution**: A concise summary of the collaborator's involvement.
- **Language** *(optional)*: The [ISO 639:2023](https://www.iso.org/standard/74575.html) code specifying the language or script (e.g., `en` for English, `zh` for Simplified Chinese). Default: `en`.
- **Standard** *(optional)*: Specify additional standards (e.g., `binary` or `ISO`).

By supporting multiple formats within the same file, `COLLABORATORS.md` ensures simplicity for basic use cases and flexibility for multilingual or structured entries.

---

## Get Involved

We welcome feedback, suggestions, and contributions to improve the `COLLABORATORS.md` standard. Feel free to:
- Open an issue to share your thoughts.
- Fork the repository and submit a pull request.

Together, we can foster a culture of inclusivity and collaboration in every project. 🌍🤝✨

---

## What's Next?

The `Collaborators` Framework is designed to grow and evolve alongside your projects. Here are some ideas to expand its use:

- **Custom Roles**: Introduce new roles tailored to your project's unique needs.
- **Integration with Tools**: Explore ways to integrate `COLLABORATORS.md` with your CI/CD pipeline or documentation workflows.
- **Community Engagement**: Share your implementation with the community to inspire others and refine the framework collectively.

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
