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

## Format

The file is structured for clarity and simplicity. Supported formats include:

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

- **Name**: The identifying name or alias of the collaborator.
- **Intent**: A controlled value describing the relationship. Shorthand options (`I`, `S`, `D`) may be used:
- **Nature**: A brief description, such as "Human" or "AI."
- **Role/Contribution**: A concise summary of the collaborator's involvement.
  - `Indirect` (I): For inspirations or influences that shaped the project.
  - `Supportive` (S): For collaborators providing critical support, such as:
      - Morale or advocacy within a community.
      - Financial sponsorship of development efforts.
      - Logistical or infrastructural support.
  - `Direct` (D): For collaborators actively and intentionally contributing to the project.
- **Language** *(optional)*: The [ISO 639:2023](https://www.iso.org/standard/74575.html) code specifying the language or script of the collaborator's entry (e.g., `en` for English, `zh` for Simplified Chinese). If omitted, the default is `en`.
- **Standard** *(optional)*: Specify an additional standard for the entry (e.g., `binary` or `ISO` for structured formats).

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
   Rob Mosher | D | Human | Creator, architect, and advocate
   ⚡🧠🤝 (Tech Vibes Companion) | Direct | AI | Collaborator and technical partner
   ```

2. **Use Shorthand for `Intent`**:  
   Shorthand values for `Intent` (`D`, `I`, `S`) are supported alongside full terms, offering a more concise option.

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

## What's Next?

The `Collaborators` Framework is designed to grow and evolve alongside your projects. Here are some ideas to expand its use:

- **Custom Roles**: Introduce new roles tailored to your project's unique needs.
- **Integration with Tools**: Explore ways to integrate `COLLABORATORS.md` with your CI/CD pipeline or documentation workflows.
- **Community Engagement**: Share your implementation with the community to inspire others and refine the framework collectively.

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
