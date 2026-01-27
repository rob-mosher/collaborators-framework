# The Collaborators Framework

**Impact Above Origin**

*Current version: v0.2.0*

## What It Is

The **Collaborators Framework** is a flexible standard for acknowledging contributions across human, AI, and hybrid collaborations. It expands the traditional view of contribution (like git authorship) to include inspiration, support, tooling, creative shaping, and more.

Use it to credit collaborators — in `COLLABORATORS.md` files or as `Collaborator:` tags in commit messages — based on their intent, nature, and role.

## How It Works

Each collaborator entry uses the following format:

```plaintext
Name | Intent | Nature | Role/Contribution | (optional: Freeform context)
```

| Field | Description |
| --- | --- |
| `Name` | Identifying name or alias of the collaborator |
| `Intent` | `Direct`: active, intentional contribution<br>`Indirect`: inspiration or shaping without direct contribution<br>`Supportive`: enabling support (morale, advocacy, funding) |
| `Nature` | Short descriptor (e.g., Human, AI, Organization, Poem) |
| `Role/Contribution` | Concise summary of involvement |
| `Freeform` | Optional personal note or context |

## Why Use It?

- **Celebrate unseen contributions**: Not all collaborators commit code — some inspire it.
- **Build inclusive histories**: Recognize everyone who shapes a project, directly or indirectly.
- **Promote intentionality**: Make space for acknowledgments that reflect your project’s values.

## Examples

### `COLLABORATORS.md`

```plaintext
Rob Mosher | Direct | Human | Creator and steward of the framework
Claude | Indirect | AI | Offered guidance on collaborative ethics
OpenAI (ChatGPT) | Direct | AI | Technical and narrative co-architect
Mary Oliver (*Wild Geese*) | Indirect | Poem by Human | Seed of inclusion | en
FooBar Initiative | Supportive | Organization | Sponsored development
```

💡 For a template, see [COLLABORATORS.md](docs/COLLABORATORS.md).

### Commit Footers

```plaintext
feat: add interactive dashboard

Collaborator: Jane Doe | Supportive | Human | Design critique and UX review  
Collaborator: Claude | Indirect | AI | Prompted the architectural insight
```

💡 For a focused, agent-friendly guide, see [collaborator-tagging-for-commits.md](docs/collaborator-tagging-for-commits.md).

## Getting Started

1. **Create a `COLLABORATORS.md`**
  Add it to your repo root.
2. **Use `Collaborator:` in commits**
  Place it in the footer, one line per collaborator.
3. **Celebrate voice**
  Let collaborators (AI or human) add their own quotes or reflections.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

🌱✨
