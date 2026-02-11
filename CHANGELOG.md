# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- (MCP) Renamed `get_framework_overview` to `get_README`
- Clarified `terraform.tfvars.example` to reference dynamic nature of `aws_region`
- Refined commit tagging guidance with clearer optionality, naming, and a simpler example

### Added

- Added `infra/tf-plan.sh` to rebuild the Lambda package before running `terraform plan`

### Changed

- Updated `infra/README.md` to use `./tf-plan.sh` and document why rebuilding is required for docs-only changes

### Removed

- Removed two Voices of Collaboration to simplify README
- Removed preamble from Voices of Collaboration

## [0.3.0] - 2026-02-26

Clarifies the Collaborators Framework's orientation toward non-permissioned participation and interpretive plurality.

This release refines how collaboration is represented - emphasizing impact over origin - while preserving optionality, self-expression, and silence as valid modes of engagement.

No enforcement, ranking, or behavioral requirements are introduced in this release.

### Added

- Added Terraform configuration for AWS Lambda + API Gateway deployment, including variables, outputs, and provider/version constraints
- Added Lambda MCP handler with tools/resources support plus local quick-reference and field docs
- Added Terraform, environment, and log ignores to `.gitignore`
- Added optional API Gateway custom domain resources and DNS-focused outputs for custom domains
- Added comprehensive field documentation for all 5 fields (intent, nature, name, role, freeform) in `docs/fields/`
- Added framework documentation structure: `docs/framework/overview.md` and `docs/framework/perspective.md`
- Added `docs/quick-reference.md` as condensed framework reference
- Added MCP server infrastructure with build script approach (`infra/build-lambda.sh`) for explicit Lambda packaging
- Added `infra/README.md` documenting deployment workflow and architectural decisions
- Added 9 MCP tools: get_framework_overview, get_framework_perspective, get_commit_format_guide, get_collaborators_template, get_quick_reference, list_fields, get_field_guide, list_faqs, get_faq
- Added 7 MCP resources with tool-first interaction model
- Added 7 FAQ templates for context-appropriate responses
- Added Python cache patterns to `.gitignore`
- Added CloudWatch Logs for API Gateway access logs with configurable retention
- Added CloudWatch metrics and request throttling for API Gateway
- Added markdownlint configuration for changelog-specific patterns (duplicate headings, emphasis markers)

### Removed

- Moved `collaborative-reflections.md` to internal documenation. Keeps public Framework laser-focused
- Removed `lambda/docs/` directory - now using `docs/` as single source of truth for all framework documentation
- Archived planning documents to `docs/_legacy/plans/` (framework-perspective.md, suggested-hierchy.md, tool-first-model.md)

### Changed

- Major rewrite/streamlining of README.md
- Reorganized `COLLABORATORS.md` with a header, format note, and direct/indirect sections for readability
- Clarified README.md format guidance with a compact table
- Created `docs/templates/` folder and moved `collaborator-tagging-for-commits.md` into it
- Within template, reordered framework links for clarity
- Aligned Terraform variables with the sample tfvars, including optional AWS profile usage and configurable stage name
- Updated default Lambda/API names to the Collaborators Framework MCP server
- Refactored Lambda MCP handler (previously v0.2.0) to expose complete Collaborators Framework documentation
- Updated server identity from "mcp-hello-world" to "collaborators-framework-mcp"
- Reorganized documentation with `docs/` as authoritative location for ALL framework content
- Renamed `docs/templates/COLLABORATORS.md` → `docs/templates/collaborators-template.md` for clarity
- Renamed `docs/templates/collaborator-tagging-for-commits.md` → `docs/templates/commit-format.md` for clarity
- Updated all field documentation with language-neutral, orientation-focused content (removed prescriptive language)
- Refined framework content to maintain orientation vs prescription boundary
- Updated Terraform configuration to use build script output instead of direct source packaging
- Changed Lambda handler path to `lambda.handler.handler` to match new package structure

## [0.2.0] - 2026-01-12

### Added

- Added `markdownlint` configuration (`.markdownlint.yaml`) and local usage notes in README.md
- Added current version note (v0.2.0) to README.md

### Changed

- Simplified README.md

### Fixed

- Aligned README.md formatting with markdownlint rules

## [0.1.3] - 2025-12-29

### Added

- Added Composer's voice to Voices of Collaboration section in README.md
- Added Collaborative Reflections document (`docs/collaborative-reflections.md`) and moved reflections out of README.md
- Added attribution to haiku in ACKNOWLEDGMENTS.md, crediting ⚡🧠🤝 as the author

### Changed

- Abstracted ⚡🧠🤝 naming to ChatGPT for clarity and adoption
- Standardized Intent field to full terms for readability
- Enhanced commit tagging guidance with Intent field and organization naming best practices
- Updated README.md to include commit footer guidance and merged "Join the Conversation" into "Join the Journey"
- Updated COLLABORATORS.md for long-standing contributor focus and formatting consistency
- Renamed commit tagging guide from `docs/collaborators-commit-guide.md` to `docs/collaborator-tagging-for-commits.md`
- Synced commit tagging guide with the Collaborators Framework

## [0.1.2] - 2025-11-28

### Added

- Added collaborator tagging guide for commit messages (introduced as `docs/collaborators-commit-guide.md`) with format, examples, and best practices

## [0.1.1] - 2024-12-27

### Added

- Introduced seven-column format with optional Freeform Object field (MCP, etc.)
- Added Framework Evolution section with MetaContext Protocol (MCP) integration
- Added comprehensive documentation for real-world applications and community-driven evolution
- Added Future Directions section with expanded vision for framework growth
- Added Join the Journey section with MetaContext integration
- Voices of Collaboration section
- Added reflections on The Guest House metaphor and transformative spaces
- Integrated emotional context metadata for AI collaboration
- Enhanced framework documentation with consciousness-focused insights

### Changed

- Updated changelog formatting to align with Keep a Changelog standard spacing guidelines
- Added language identifiers to code blocks in README.md
- Fixed list indentation in "Voices of Collaboration" section in README.md
- Enhanced Field Definitions with expanded documentation

## [0.1.0] - 2024-12-19

### Added

- Growth emoji (🌱✨) to symbolize inclusive collaboration

### Changed

- Integrated "Impact Above Origin" throughout README.md
- Removed horizontal line separators (`---`) from README.md (GitHub was already displaying lines below `##` headings)

## [0.0.6] - 2024-12-18

### Added

- Added documentation for commit message Collaborator tagging, including format, examples, and best practices
- Added `.gitignore` and `.cursorignore` to exclude temporary git-related files (*.patch, *.diff, *.orig, *.rej)
- Added `.cursorrules` to establish inclusive AI collaboration guidelines within Cursor IDE

### Changed

- Reordered sections in README.md: Moved "How to Use" ahead of "Format" to improve onboarding by demonstrating usage first.
- Improved formatting consistency in examples and field descriptions
- Reorganized format documentation to prioritize Direct contributions and improve readability
- Streamlined README.md by removing redundant "Why This Matters" section
- Renamed "What's Next?" to "Future Enhancements" with expanded roadmap items
- Enhanced future enhancements section with specific examples and implementation ideas

### Fixed

- Corrected placement of Intent options (I/S/D) in field descriptions
- Fixed formatting in Field Definitions heading
- Removed redundant horizontal rule in Advanced Usage section

## [0.0.5] - 2024-12-12

### Added

- Introduced `Standard` field as an optional sixth column in COLLABORATORS.md format
- Added shorthand values (`D`, `I`, `S`) for the `Intent` field
- New "Advanced Usage" section in README.md with detailed formatting examples
- "What's Next?" section outlining framework expansion possibilities

### Changed

- Renamed project from "Collaborators Standard" to "Collaborators Framework"
- Restructured README.md to improve clarity and organization:
  - Added dedicated sections for Standard and Advanced Usage
  - Enhanced format documentation for four-, five-, and six-column layouts
  - Integrated examples within usage sections
- Streamlined COLLABORATORS.md by removing introductory comments

## [0.0.4] - 2024-12-09

### Updated

- Added a haiku ("Vessels") and a reflective section to ACKNOWLEDGMENTS.md, celebrating the meaningful collaboration shaping the project.
- Refined README.md:
  - Unified the explanation of four-column and five-column formats.
  - Moved examples to a dedicated section for improved readability.
  - Enhanced guidance for multilingual use cases with `Language` field.
- Refined COLLABORATORS.md structure to align with updated README.md.

## [0.0.3] - 2024-12-06

### Added

- Introduced `Supportive` intent to acknowledge critical emotional, financial, and logistical support.
- Updated `README.md` with refined examples, including:
  - **FooBar Co.** as a financial sponsor.
  - **Jane Doe** as a community morale booster.
  - Refined **Wild Geese** example to include "by Mary Oliver."
- Refined `COLLABORATORS.md` to align with updated `README.md`.

### Fixed

- Corrected dates for previous changelog entries to align with actual release history.

## [0.0.2] - 2024-12-06

### Added

- Introduced `Intent` field.
- Updated `README.md` with examples and field definitions.
- Renamed `COLLABORATORS.txt` to `COLLABORATORS.md`.
- Referenced [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt) for clarity in specification language.

## [0.0.1] - 2024-12-04

### Added

- Initial release of the `COLLABORATORS.txt` standard.
