# Collaborators Framework Quick Reference

## Format

```
Name | Intent | Nature | Role/Contribution | Freeform (optional)
```

## Field Definitions

| Field | Values/Examples | Required |
|-------|-----------------|----------|
| **Name** | Identifying name or alias | Yes |
| **Intent** | `Direct`, `Indirect`, `Supportive` | Yes |
| **Nature** | Human, AI, Organization, Poem, Tool, etc. | Yes |
| **Role** | Summary of contribution | Yes |
| **Freeform** | Personal note or context | No |

### Intent Values

- **Direct**: Active, intentional contribution (code, design, pair programming)
- **Indirect**: Inspiration without direct contribution (conversation, artwork, blog post)
- **Supportive**: Enabling support (morale, funding, infrastructure)

### Nature Examples

Human, AI (Claude), AI (ChatGPT), Organization, Poem by Human, Tool, System, Concept, Book, Film, Song

## Usage Contexts

### 1. COLLABORATORS.md File

Repository-level acknowledgment file listing all collaborators.

**Example:**
```
Rob Mosher | Direct | Human | Creator and steward of the framework
Claude (Anthropic) | Indirect | AI | Collaborative ethics guidance
Mary Oliver (*Wild Geese*) | Indirect | Poem by Human | Seed of inclusion
```

### 2. Commit Footers

`Collaborator:` prefix, one per line.

**Example:**
```
feat: add user profile page

Adds the user profile page with a welcoming, minimalist layout.

Collaborator: Jane Doe | Direct | Human | Initial component structure
Collaborator: Claude | Indirect | AI | Architectural insight
```

## Principle

**Impact Above Origin**

Contributions are understood in terms of how they shape outcomes, not where they come from.

## Resources

- Full documentation: `collaborators://framework/README`
- Commit guide: `collaborators://templates/commit-format`
- Field details: `collaborators://field/{name}`
