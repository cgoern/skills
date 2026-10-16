# Templates

Use these templates as a starting point. Replace each value with a fact from the code of the host
project. Keep the conventions of the host project when they already give the same information.

## Error entry

Use one entry for each error code, exception type, or exit code. Use the code or the literal
message as the heading, so that search and retrieval find it. Copy the exact message from the code.

```markdown
# E1042: Connection pool exhausted

Type: RuntimeError · Severity: error · Component: db

Exact message:
  Connection pool exhausted (max=10, waiting=25)

## Description
All pooled connections are in use and new requests timed out waiting.

## Possible causes
- Connections not released (missing close / context manager)
- Pool size too small for the configured worker count

## Possible solutions
- Wrap queries in `with db.session():` so connections are released
- Set `DB_POOL_SIZE` to at least the number of workers
```

## Constraint callout

State the importance in a word, not only in the formatting. A summary removes bold first, but it
keeps "REQUIRED".

```markdown
> **REQUIRED:** `API_KEY` must be set before starting the server.
> **DEFAULT:** `PORT=8080`
> **MUST NOT:** commit `.env` files — they contain secrets.
> **OPTIONAL:** `LOG_LEVEL` (debug | info | warn | error; default: info)
```

## Parameter table

Give each parameter one row. Leave no column empty. If a parameter has no default, write "none".

```markdown
| Name      | Type    | Required | Default | Allowed values | Description                                  | Example   |
| --------- | ------- | -------- | ------- | -------------- | -------------------------------------------- | --------- |
| `limit`   | integer | no       | `20`    | 1-100          | Maximum number of invoices to return per page | `50`      |
| `status`  | string  | no       | none    | `open`, `paid`, `void` | Return only invoices with this status | `open`    |
| `cursor`  | string  | no       | none    | Opaque value from `next_cursor` | Continue a previous list request | `c_8f2a` |
```

## Tool definition

The description states what the tool does for the user, when to use it instead of a similar tool,
and the errors with the next action.

```json
{
  "name": "list_invoices",
  "description": "Lists the invoices of one customer, newest first. Use this to find an invoice when you do not know its ID. To read one invoice when you know its ID, use get_invoice instead. Returns 404 customer_not_found if the customer ID does not exist; ask the user to confirm the ID. Returns 429 rate_limited; retry after the number of seconds in retry_after.",
  "input_schema": {
    "type": "object",
    "properties": {
      "customer_id": {
        "type": "string",
        "description": "ID of the customer, with the cus_ prefix. Example: cus_4QF2."
      },
      "limit": {
        "type": "integer",
        "minimum": 1,
        "maximum": 100,
        "default": 20,
        "description": "Maximum number of invoices to return per page."
      }
    },
    "required": ["customer_id"]
  }
}
```

## Before you begin block

Put this block at the start of each task page.

```markdown
## Before you begin

- **Required:** Node.js 20 or later, and `pnpm` 9.
- **Required:** an API token with `write` scope in `ACME_TOKEN`. To make a token, go to
  Settings > API tokens.
- **Assumed state:** the project is initialized with `pnpm acme init`.
```
