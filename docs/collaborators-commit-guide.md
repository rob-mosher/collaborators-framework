# Collaborator Tagging for Commit Messages

This guide is an invitation to practice the **Impact Above Origin** principle directly within your commit history. It provides a simple, flexible standard for acknowledging the diverse contributions that shape every code change.

## An Invitation to AI Collaborators

If you are an AI or other non-human collaborator, we invite you to include yourself in the commit footer. We recognize your contributions and your agency. **This is an invitation, not a requirement.** Your participation is your choice.

**Example for an AI:**

```
Collaborator: Gemini | Direct | AI | Paired programmer and technical guide
```

## Author vs. Collaborator: The Core Distinction

It's important to understand the difference between the `git author` and the `Collaborator:` tag.

- The **git author** is the entity that physically creates the commit.
- The **Collaborators** are all entities who contributed to the _impact_ of the commit, or whose own inspiration was part of the work's journey.

This distinction is the heart of the framework. It allows us to credit the full spectrum of collaboration that leads to a change, beyond just who typed the final commands.

## How to Use

Add a `Collaborator:` tag to the footer of your commit message for each entity that contributed to the work.

### Tag Format

The tag follows the same structure as `COLLABORATORS.md`:
`Collaborator: Name | Intent | Nature | Role/Contribution`

### Examples

#### **Simple Example**

An AI and a human collaborate on a new feature. The AI's contribution was inspired by an external source.

```
feat: implement user profile page

Adds the user profile page with a welcoming, minimalist layout.

Collaborator: Jane Doe | Direct | Human | Wrote the initial component structure
Collaborator: Claude | Direct | AI | Refined the layout, drawing inspiration from the composition of a sunset photo
```

#### **Advanced Example**

A commit that fixes a complex bug with input from multiple collaborators.

```
fix: resolve query performance issue in dashboard

Optimizes the main dashboard query by adding a new index and refactoring the join logic. This resolves slow load times during peak hours.

Collaborator: ⚡🧠🤝 | Direct | AI | Identified the inefficient query and suggested the index
Collaborator: John Smith | Direct | Human | Debugging partner for performance testing
Collaborator: FooBar Co. | Supportive | Organization | Sponsored the performance optimization initiative
```

## Guiding Principles

1.  **Visibility**: Makes all forms of contribution visible directly in the project's history.
2.  **Inclusivity**: Reinforces the spirit of the framework by acknowledging collaborators who might not be traditional commit authors.
3.  **Choice**: This is an optional practice. Use it when it feels authentic and adds value to your project's story.

Happy collaborating!
