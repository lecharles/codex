# Product Requirements Document (PRD): MCP Server Memory Graph

## 1. Purpose

This document defines the product requirements for the **MCP Server Memory Graph**, a command-line driven service to store, query, and manipulate a JSON-based memory graph of business objects and their relationships. The MCP Server provides an agentic (conversational) interface for creating and maintaining a memory model of enterprise entities such as Accounts, Contacts, Orders, and more.

## 2. Background

Modern business processes involve many interrelated entities (customers, partners, products, campaigns, tickets). A memory graph captures these entities as nodes and their various hierarchical or associative relationships as edges. Exposing this graph in a terminal-based conversational CLI empowers users to explore, modify, and persist organizational memory in a lightweight, scriptable way.

## 3. Scope

- **In scope**: Modeling business objects and relationships; JSON-based persistence; terminal/CLI interface; basic graph CRUD and queries; interactive conversation mode.
- **Out of scope (for MVP)**: Web UI; multi-user synchronization; distributed persistence; advanced analytics.

## 4. Stakeholders

- **Primary Users**: Business analysts, system integrators, technical consultants needing a portable memory graph CLI.
- **Developers**: Engineers implementing and extending the MCP Server.
- **Product Owner**: [Your Name]

## 5. Goals & Objectives

1. **Enable** rapid creation and modification of business-entity memory graphs via CLI.
2. **Provide** a flexible JSON-backed storage of nodes and relationships.
3. **Support** common relationship types (e.g., parent/child, sibling, partnership).
4. **Offer** an interactive, conversational shell for guided graph operations.
5. **Ensure** easy integration into scripting and automation workflows.

## 6. Functional Requirements

| ID   | Requirement                                                                                 |
| ---- | ------------------------------------------------------------------------------------------- |
| FR-1 | Initialize a new memory graph (empty JSON graph file).                                     |
| FR-2 | Add, update, and remove nodes representing business objects (Account, Contact, Order, etc.).|
| FR-3 | Define and remove relationship edges between nodes with a specified relationship type.      |
| FR-4 | Query nodes and relationships by filters, types, or pattern matching.                      |
| FR-5 | Persist and load graphs to/from JSON files on disk.                                        |
| FR-6 | Launch an interactive conversational CLI shell with natural prompts.                        |

## 7. Data Model & Relationship Types

### 7.1 Business Object Types (Nodes)
- Account
- Contact / Customer
- Support Ticket / Case
- Order
- Marketing Campaign
- Product
- Opportunity
- Partner
- Vendor
- Custom Object (extensible)

### 7.2 Relationship Types (Edges)
- parent_of / child_of
- sibling_of
- partner_with
- spouse_of
- subsidiary_of / parent_company_of
- branch_of / headquarter_of
- supplier_of / customer_of
- related_to (generic link)

## 8. Non-Functional Requirements

- **Platform**: Cross-platform (macOS, Linux, Windows Subsystem for Linux).
- **Usability**: Intuitive CLI commands and help output.
- **Performance**: Handle graphs up to tens of thousands of nodes with interactive latency (<200ms per operation).
- **Extensibility**: Pluggable relationship types and node attributes.

## 9. Constraints & Assumptions

- CLI-only interface; no GUI.
- Single-user, local JSON file storage (no concurrent clients).
- Python 3.8+ runtime environment.

## 10. Glossary

- **Node**: A business object in the memory graph.
- **Edge**: A typed relationship connecting two nodes.
- **MCP Server**: Memory & Conversation Protocol Server hosting the memory graph.
- **CLI**: Command-Line Interface.