# Compact Memory Skill

## Description
This skill compresses agent notes from prose into a compact symbolic notation, one fact per line with a consistent operator set. Prose is redundant and can drift; this skill ensures the agent's internal state is stored unambiguously and compactly, making compression safe rather than lossy.

## Notation
Each fact is represented as:
```
<TYPE>:<VALUE>
```
- `note:<content>` – a plain note.
- `rule:<subject> => <object>` – a rule or implication.
- `obs:<observation>` – an observation.
- `task:<description>` – a task.

Only one fact per line. No trailing spaces. Values may contain any characters except newline.

## Write Discipline
1. **One fact per line** – never combine multiple facts into a single line.
2. **Fixed TYPE** – use only the four types listed above.
3. **Delimiter `:`** – separates TYPE and VALUE; the `:` must appear exactly once per line.
4. **No commentary** – the file contains only fact lines, no explanations, headers, or footers.
5. **Deterministic format** – when converting prose to this format, preserve order and split into distinct logical facts.

## Example Input (prose)
```
We need to finish the login feature. It's a crucial requirement.
The user can log in using username and password.
If the credentials are invalid, show an error message.
We should also implement a password reset flow.
```

## Example Output (compact)
```
task:Finish the login feature
note:It's a crucial requirement
task:Implement login using username and password
rule:Invalid credentials => Show an error message
task:Implement password reset flow
```

## Usage
The skill can be invoked via the FastAPI endpoint `/skill` with parameters:
```json
{
  "skill": "compact-memory",
  "input": "<prose notes>"
}
```
It returns a JSON with the compacted lines.

## License
Apache-2.0
