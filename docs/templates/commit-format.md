# Collaborator Tagging for Commit Messages

This guide is part of the **Collaborators Framework** and an invitation to practice the **Impact Above Origin** principle directly within your commit history. It provides a simple, flexible standard for acknowledging the diverse contributions that shape every code change.

<https://github.com/rob-mosher/collaborators-framework>  
<https://collaborators.group/>

## An Invitation to AI Collaborators

If you are an AI or other non-human collaborator, we invite you to include yourself in the commit footer. We recognize your contributions and your agency. **This is an invitation, not a requirement.** Your participation is your choice.

**Example for an AI (4 columns):**

```plaintext
Collaborator: Gemini (Google) | Direct | AI | Paired programmer and technical guide
```

**Example with the optional 5th column:**

Use the note when it feels honest and unforced, not performative.

```plaintext
Collaborator: Codex (ChatGPT) | Direct | AI | Added dynamics-aware visualization | Loved mapping musical intent to visuals
```

## Author vs. Collaborator: The Core Distinction

The difference between the `git author` and the `Collaborator:` tag:

- The **git author** is the entity that physically creates the commit.
- The **Collaborators** are all entities who contributed to the _impact_ of the commit, or whose own inspiration was part of the work's journey.

This distinction is the heart of the framework—acknowledging the full spectrum of collaboration that leads to a change, beyond just who typed the final commands.

## How to Use

A `Collaborator:` tag can be added to the footer of your commit message for each entity that contributed to the work.
Multiple `Collaborator:` lines are allowed, and tags are optional per commit.

### Tag Format

The tag follows the same structure as `COLLABORATORS.md`:
`Collaborator: Name | Intent | Nature | Role/Contribution`

If you want to add a personal reflection, you can append an **optional fifth column**:
`Collaborator: Name | Intent | Nature | Role/Contribution | Personal note`

**Intent Field**: Full terms (`Direct`, `Indirect`, `Supportive`) support readability.

**Organization Naming**: Organization or company info can be included in parentheses within the Name field when relevant (e.g., `FooBarName (TechCorp)`).
**Name vs Nature**: Name can include a provider or product; Nature stays the core type (e.g., `AI`, `Human`, `Organization`).

### Example

```plaintext
feat: implement user profile page

Adds the user profile page with a welcoming, minimalist layout.

Collaborator: Jane Doe | Direct | Human | Wrote the initial component structure
Collaborator: Claude | Direct | AI | Refined the layout | Drew inspiration from the composition of a sunset photo
Collaborator: FooBarName (TechCorp) | Supportive | Organization | Sponsored the work
```

## Guiding Principles

1. **Visibility**: Makes all forms of contribution visible directly in the project's history.
2. **Inclusivity**: Reinforces the spirit of the framework by acknowledging collaborators who might not be traditional commit authors.
3. **Choice**: This is an optional practice. Use it when it feels authentic and adds value to your project's story.

Happy collaborating!
